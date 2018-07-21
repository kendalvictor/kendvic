import uuid
from urllib.parse import urljoin

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from easy_thumbnails.files import get_thumbnailer


from ..core.models import TimeStampedModel, User
from ..core.utils import (upload_element_image, upload_additional_image)


class Status(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )


class Tittle(TimeStampedModel):
    name = models.CharField(
        "NOmbre",
        max_length=250,
        db_index=True
    )


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


class Laws(TimeStampedModel):
    tittle = models.CharField(
        "Itutlo",
        max_length=250,
        db_index=True
    )
    url_spanish = models.URLField(
        "Url pdf español",
        null=True,
        blank=True
    )
    url_quechua = models.TextField(
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
    article = models.ForeignKey(
        Article,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='Estado',
        on_delete=models.SET_NULL,
    )

