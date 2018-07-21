import uuid
from urllib.parse import urljoin

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from easy_thumbnails.files import get_thumbnailer


from ..core.models import TimeStampedModel, User
from ..core.utils import (upload_element_image, upload_additional_image)


class Comision(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Comision"
        verbose_name_plural = u"Comision"


class Status(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Estado"
        verbose_name_plural = u"Estados"


class Tittle(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Titulo"
        verbose_name_plural = u"Titulos"


class Chapter(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )
    title = models.ForeignKey(
        Tittle,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Titulo',
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Capitulo"
        verbose_name_plural = u"Capitulos"


class Article(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )
    chapter = models.ForeignKey(
        Chapter,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Capitulo',
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Articulo"
        verbose_name_plural = u"Articulos"


class Laws(TimeStampedModel):
    code = models.CharField(
        "Codigo/Numero",
        max_length=250,
        db_index=True
    )
    tittle = models.CharField(
        "Titulo de la ley",
        max_length=250,
        db_index=True
    )
    published = models.DateField(
        'Fecha de PUblicacion',
        null=True,
        blank=True
    )
    url_spanish = models.URLField(
        "Url pdf español",
        null=True,
        blank=True
    )
    url_quechua = models.URLField(
        "Url pdf quechua",
        null=True,
        blank=True
    )
    status = models.ForeignKey(
        Status,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Estado',
        on_delete=models.SET_NULL,
    )
    comision = models.ForeignKey(
        Comision,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Comision',
        on_delete=models.SET_NULL,
    )
    article = models.ForeignKey(
        Article,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Estado',
        on_delete=models.SET_NULL,
    )
    chapter = models.ForeignKey(
        Chapter,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Capitulo',
        on_delete=models.SET_NULL,
    )
    title_legis = models.ForeignKey(
        Tittle,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Titulo Legislativo',
        on_delete=models.SET_NULL,
    )
    displeases = models.IntegerField(
        default=0
    )
    like = models.IntegerField(
        default=0
    )
    comments = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = u"Ley"
        verbose_name_plural = u"Leyes"


class Questions(TimeStampedModel):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Usuario',
        on_delete=models.SET_NULL,
    )
    text = models.TextField(
        "Respuesta",
    )
    law = models.ForeignKey(
        Laws,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Ley',
        on_delete=models.SET_NULL,
    )
    approved = models.BooleanField(
        default=False
    )
    displeases = models.IntegerField(
        default=0
    )
    like = models.IntegerField(
        default=0
    )
    comments = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u"Pregunta"
        verbose_name_plural = u"Preguntas"


class Answer(TimeStampedModel):
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Usuario',
        on_delete=models.SET_NULL,
    )
    question = models.ForeignKey(
        Questions,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Pregunta',
        on_delete=models.SET_NULL,
    )
    text = models.CharField(
        "Pregunta",
        max_length=250,
        db_index=True
    )
    law = models.ForeignKey(
        Laws,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Ley',
        on_delete=models.SET_NULL,
    )
    approved = models.BooleanField(
        default=False
    )
    counter = models.BooleanField(
        'Contado',
        default=False
    )
    displeases = models.IntegerField(
        default=0
    )
    like = models.IntegerField(
        default=0
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u"Respuesta"
        verbose_name_plural = u"Respuestas"