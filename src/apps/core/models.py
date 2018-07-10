# coding=utf-8
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'Creado',
        default=timezone.now,
        null=True,
        blank=True
    )
    modified = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Correo electrónico',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True
    )
    is_admin = models.BooleanField(
        'Admin',
        default=False
    )
    points = models.IntegerField(
        "Puntos",
        default=0
    )
    first_name = models.CharField(
        'Nombres',
        max_length=200,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        'Apellidos',
        max_length=200,
        null=True,
        blank=True
    )
    dni = models.CharField(
        'DNI',
        max_length=8,
        blank=False,
        null=True,
        unique=True
    )
    tlf = models.CharField(
        'Celular',
        max_length=15,
        blank=True,
        null=True,
    )
    address = models.TextField(
        'Dirección',
        blank=True,
        null=True
    )
    birth_date = models.DateField(
        'Fecha de nacimiento',
        null=True,
        blank=True
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['date_of_birth']

    class Meta:
        verbose_name = u'Usuario'

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        else:
            return self.email

    def save(self, *args, **kwargs):
        self.email = self.email.lower().strip()
        if self.first_name:
            self.first_name = self.first_name.title().strip()
        if self.last_name:
            self.last_name = self.last_name.title().strip()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


