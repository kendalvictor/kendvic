from django.core.validators import RegexValidator
from django.db import models


class UbigeoContinente(models.Model):
    cod_ubigeo_reniec_continente = models.CharField(
        'Código Ubigeo Continente - RENIEC', max_length=2,
        validators=[
            RegexValidator(
                regex='^[0-9]{1,2}$',
                message='Numero de 1 o 2 digitos',
            ),
        ], null=False, blank=False)
    cod_ubigeo_inei_continente = models.CharField(
        'Código Ubigeo Continente - INEI', max_length=2,
        validators=[
            RegexValidator(
                regex='^[0-9]{1,2}$',
                message='Numero de 1 o 2 digitos',
            ),
        ], null=False, blank=False)
    ubigeo_continente = models.CharField(
        'Nombre Ubigeo Continente', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.ubigeo_continente

    class Meta:
        verbose_name_plural = '1. Ubigeo Continentes'


class UbigeoPais(models.Model):
    cod_ubigeo_reniec_pais = models.CharField(
        'Código Ubigeo Pais - RENIEC', max_length=3,
        validators=[
            RegexValidator(
                regex='^[0-9]{1,3}$',
                message='Numero de 1 o 3 digitos',
            ),
        ], null=False, blank=False)
    cod_ubigeo_inei_pais = models.CharField(
        'Código Ubigeo Pais - INEI', max_length=3,
        validators=[
            RegexValidator(
                regex='^[0-9]{1,3}$',
                message='Numero de 1 o 3 digitos',
            ),
        ], null=False, blank=False)
    ubigeo_pais = models.CharField(
        'Nombre Ubigeo Pais', max_length=100, null=False, blank=False)
    continente = models.ForeignKey(
        UbigeoContinente, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_continente')

    def __str__(self):
        return self.ubigeo_pais

    class Meta:
        verbose_name_plural = '2. Ubigeo Paises'


class UbigeoDepartamento(models.Model):
    cod_ubigeo_reniec_departamento = models.CharField(
        'Código Ubigeo Departamento - RENIEC', max_length=2,
        validators=[
            RegexValidator(
                regex='^[0-9]{2}$',
                message='Numero de 2 digitos',
            ),
        ], null=False, blank=False)
    cod_ubigeo_inei_departamento = models.CharField(
        'Código Ubigeo Departamento - INEI', max_length=2,
        validators=[
            RegexValidator(
                regex='^[0-9]{2}$',
                message='Numero de 2 digitos',
            ),
        ], null=False, blank=False)
    ubigeo_departamento = models.CharField(
        'Nombre Ubigeo Departamento', max_length=100, null=False, blank=False)
    continente = models.ForeignKey(
        UbigeoContinente, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_continente')
    pais = models.ForeignKey(
        UbigeoPais, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_pais')

    def __str__(self):
        return self.ubigeo_departamento

    class Meta:
        verbose_name_plural = '3. Ubigeo Departamentos'


class UbigeoProvincia(models.Model):
    cod_ubigeo_reniec_provincia = models.CharField(
        'Código Ubigeo Provincia - RENIEC', max_length=4,
        validators=[
            RegexValidator(
                regex='^[0-9]{4}$',
                message='Numero de 4 digitos',
            ),
        ], null=False, blank=False)
    cod_ubigeo_inei_provincia = models.CharField(
        'Código Ubigeo Provincia - INEI', max_length=4,
        validators=[
            RegexValidator(
                regex='^[0-9]{4}$',
                message='Numero de 4 digitos',
            ),
        ], null=False, blank=False)
    ubigeo_provincia = models.CharField(
        'Nombre Ubigeo Provincia', max_length=100, null=False, blank=False)
    continente = models.ForeignKey(
        UbigeoContinente, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_continente')
    pais = models.ForeignKey(
        UbigeoPais, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_pais')
    departamento = models.ForeignKey(
        UbigeoDepartamento, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_departamento')

    def __str__(self):
        return self.ubigeo_provincia

    class Meta:
        verbose_name_plural = '4. Ubigeo Provincias'


class UbigeoDistrito(models.Model):
    cod_ubigeo_reniec_distrito = models.CharField(
        'Código Ubigeo Distrito - RENIEC', max_length=6,
        validators=[
            RegexValidator(
                regex='^[0-9]{6}$',
                message='Numero de 6 digitos',
            ),
        ], null=False, blank=False)
    cod_ubigeo_inei_distrito = models.CharField(
        'Código Ubigeo Distrito - INEI', max_length=6,
        validators=[
            RegexValidator(
                regex='^[0-9]{6}$',
                message='Numero de 6 digitos',
            ),
        ], null=False, blank=False)
    ubigeo_distrito = models.CharField(
        'Nombre Ubigeo Distrito', max_length=100, null=False, blank=False)
    continente = models.ForeignKey(
        UbigeoContinente, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_continente')
    pais = models.ForeignKey(
        UbigeoPais, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_pais')
    departamento = models.ForeignKey(
        UbigeoDepartamento, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_departamento')
    provincia = models.ForeignKey(
        UbigeoProvincia, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_provincia')

    def __str__(self):
        return self.ubigeo_distrito

    class Meta:
        verbose_name_plural = '5. Ubigeo Distritos'


class UbigeoLocalidad(models.Model):
    cod_ubigeo_reniec_localidad = models.CharField(
        'Código Ubigeo Localidad - RENIEC', max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{8,10}$',
                message='Numero entre 8 y 10 digitos',
            ),
        ], null=False, blank=False)
    cod_ubigeo_inei_localidad = models.CharField(
        'Código Ubigeo Localidad - RENIEC', max_length=10,
        validators=[
            RegexValidator(
                regex='^[0-9]{8,10}$',
                message='Numero entre 8 y 10 digitos',
            ),
        ], null=False, blank=False)
    ubigeo_localidad = models.CharField(
        'Nombre Ubigeo Localidad', max_length=100, null=False, blank=False)
    continente = models.ForeignKey(
        UbigeoContinente, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_continente')
    pais = models.ForeignKey(
        UbigeoPais, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_pais')
    departamento = models.ForeignKey(
        UbigeoDepartamento, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_departamento')
    provincia = models.ForeignKey(
        UbigeoProvincia, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_provincia')
    distrito = models.ForeignKey(
        UbigeoDepartamento, on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_distrito')

    def __str__(self):
        return self.ubigeo_localidad

    class Meta:
        verbose_name_plural = '6. Ubigeo Localidades'
