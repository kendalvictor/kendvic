from dal import autocomplete

from django import forms
from .models import Laws


class LawHomeForm(forms.ModelForm):
    class Meta:
        model = Laws
        fields = ('tittle',)
        widgets = {
            'tittle': autocomplete.ModelSelect2(url='law-autocomplete')
        }