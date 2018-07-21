# coding=utf-8
from django.conf.urls import url

from discapacitados.ubigeo.api.views import (
    DetalleUbigeoContinenteAPI, DetalleUbigeoDepartamentoAPI,
    DetalleUbigeoDistritoAPI, DetalleUbigeoPaisAPI, DetalleUbigeoProvinciaAPI,
    ListaUbigeoContinenteAPI, ListaUbigeoDepartamentoAPI,
    ListaUbigeoDistritoAPI, ListaUbigeoPaisAPI, ListaUbigeoProvinciaAPI)

urlpatterns = [
    url(r'^ubigeo/$', ListaUbigeoContinenteAPI.as_view()),
    url(r'^ubigeo/(?P<cod_continente>\w{1,2})/$', ListaUbigeoPaisAPI.as_view()),
    url(r'^ubigeo/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/$',
        ListaUbigeoDepartamentoAPI.as_view()),
    url(
        r'^ubigeo/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/(?P<cod_departamento>\w{2})/$',
        ListaUbigeoProvinciaAPI.as_view()),

    url(
        r'^ubigeo/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/(?P<cod_departamento>\w{2})/(?P<cod_provincia>\d{4})/$',
        ListaUbigeoDistritoAPI.as_view()),
    # -- detalles
    url(r'^ubigeo/detalle/(?P<cod_continente>\w{1,2})/$',
        DetalleUbigeoContinenteAPI.as_view()),
    url(r'^ubigeo/detalle/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/$',
        DetalleUbigeoPaisAPI.as_view()),
    url(
        r'^ubigeo/detalle/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/(?P<cod_departamento>\w{2})/$',
        DetalleUbigeoDepartamentoAPI.as_view()),
    url(
        r'^ubigeo/detalle/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/(?P<cod_departamento>\w{2})/(?P<cod_provincia>\d{4})/$',
        DetalleUbigeoProvinciaAPI.as_view()),
    url(
        r'^ubigeo/detalle/(?P<cod_continente>\w{1,2})/(?P<cod_pais>\w{1,2})/(?P<cod_departamento>\w{2})/(?P<cod_provincia>\d{4})/(?P<cod_distrito>\d{6})/$',
        DetalleUbigeoDistritoAPI.as_view()),
]
