import time

from django.conf import settings
from django.urls import path, re_path
from django.views.generic import TemplateView


STATIC_HASH = hash(time.time())


urlpatterns = [
    path(
        r'portada/',
        TemplateView.as_view(
            template_name='index.html',
            extra_context={
                'STATIC_HASH': STATIC_HASH,
                'SITE_URL': settings.SITE_URL
            }
        )
    ),
]
