
from django.conf.urls import url, include
from .views import get_laws

urlpatterns = [
    url(
        r'^list/$',
        get_laws,
        name='laws',
    ),
]