# coding=utf-8

import os
from django.utils.text import slugify
from datetime import datetime
from django.utils import timezone


def upload_additional_image(instance, filename, path='image/%Y/%m/%d'):

    path = timezone.localtime().strftime(path)
    name = slugify(instance.text)[:75]
    extension = filename.split('.').pop()
    filename = "{0}-{1}-{2}.{3}".format(
        name, instance.kind, instance.id, extension)
    return os.path.join(path, filename)


def upload_element_image(instance, filename, path='alternatives/%Y/%m/%d'):
    path = timezone.localtime().strftime(path)
    name = slugify(instance.question.text)[:75]
    extension = filename.split('.').pop()
    filename = "{0}-{1}.{2}".format(
        name, instance.question.id, extension)
    return os.path.join(path, filename)
