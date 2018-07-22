# coding=utf-8

import re
import requests
from datetime import datetime, timedelta

from django.db.models import Count
from django import template
from django.conf import settings as global_settings
from django.core.cache import cache

from ..models import Laws, Questions

register = template.Library()


@register.simple_tag()
def get_most_answered():
    return Laws.objects.all().order_by('-comments')[:3]


@register.simple_tag()
def get_most_like():
    return Laws.objects.all().order_by('-like')[:3]


@register.simple_tag()
def get_last_answered():
    return Laws.objects.all().order_by('-last_answer')[:3]