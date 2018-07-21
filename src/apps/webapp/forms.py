from dal import autocomplete

from django import forms
from apps.legislativo.models import Laws


class LawHomeForm(forms.ModelForm):
    class Meta:
        model = Laws
        fields = ('tittle',)
        widgets = {
            'tittle': forms.TextInput(attrs={
                'class': "form-control",
                'type': 'search',
                'placeholder': 'Ingresa ley'
            })
        }