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


class TwiterForm(forms.Form):
    twiter = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['twiter'].widget.attrs.update(
            {'class': 'form-control', 'style': 'width:400px;', 'placeholder':'Ingrese Hastag'})


from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('email')
        if username and not User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario no existe')
        return username

