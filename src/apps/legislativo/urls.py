from .widgets import LawsAutocomplete
from django.conf.urls import url, include

urlpatterns = [
    url(
        r'^law-autocomplete/$',
        LawsAutocomplete.as_view(),
        name='law-autocomplete',
    ),
]