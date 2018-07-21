# coding=utf-8
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from discapacitados.ubigeo.api.serializers import \
    DetalleUbigeoContinenteSerializer, DetalleUbigeoDepartamentoSerializer, \
    DetalleUbigeoDistritoSerializer, DetalleUbigeoPaisSerializer, \
    DetalleUbigeoProvinciaSerializer, \
    ListaUbigeoContienteSerializer, ListaUbigeoDepartamentoSerializer, \
    ListaUbigeoDistritoSerializer, \
    ListaUbigeoPaisSerializer, ListaUbigeoProvinciaSerializer
from discapacitados.ubigeo.models import UbigeoContinente, UbigeoDepartamento, \
    UbigeoDistrito, UbigeoPais, UbigeoProvincia


class ListaUbigeoContinenteAPI(ListAPIView):
    serializer_class = ListaUbigeoContienteSerializer

    def get_queryset(self):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        return UbigeoContinente.objects.all()

    def provider_reniec(self):
        return UbigeoContinente.objects.all()


class ListaUbigeoPaisAPI(ListAPIView):
    serializer_class = ListaUbigeoPaisSerializer
    paginate_by = 200

    def get_queryset(self):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        continente = get_object_or_404(UbigeoContinente,
                                       cod_ubigeo_inei_continente=self.kwargs.get(
                                           'cod_continente', ''))
        return UbigeoPais.objects.filter(continente=continente)

    def provider_reniec(self):
        continente = get_object_or_404(UbigeoContinente,
                                       cod_ubigeo_reniec_continente=self.kwargs.get(
                                           'cod_continente', ''))
        return UbigeoPais.objects.filter(continente=continente)


class ListaUbigeoDepartamentoAPI(ListAPIView):
    serializer_class = ListaUbigeoDepartamentoSerializer
    paginate_by = 100

    def get_queryset(self):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        continente = get_object_or_404(
            UbigeoContinente,
            cod_ubigeo_inei_continente=self.kwargs.get('cod_continente', ''))
        pais = get_object_or_404(
            UbigeoPais,
            cod_ubigeo_inei_pais=self.kwargs.get('cod_pais', ''),
            continente=continente)
        return UbigeoDepartamento.objects.filter(
            continente=continente, pais=pais)

    def provider_reniec(self):
        continente = get_object_or_404(
            UbigeoContinente,
            cod_ubigeo_reniec_continente=self.kwargs.get('cod_continente', ''))
        pais = get_object_or_404(
            UbigeoPais, cod_ubigeo_reniec_pais=self.kwargs.get('cod_pais', ''),
            continente=continente)
        return UbigeoDepartamento.objects.filter(
            continente=continente, pais=pais)


class ListaUbigeoProvinciaAPI(ListAPIView):
    serializer_class = ListaUbigeoProvinciaSerializer
    paginate_by = 100

    def get_queryset(self):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        continente = get_object_or_404(
            UbigeoContinente,
            cod_ubigeo_inei_continente=self.kwargs.get('cod_continente', ''))
        pais = get_object_or_404(
            UbigeoPais,
            cod_ubigeo_inei_pais=self.kwargs.get('cod_pais', ''),
            continente=continente)
        departamento = get_object_or_404(
            UbigeoDepartamento,
            cod_ubigeo_inei_departamento=self.kwargs.get('cod_departamento',''),
            continente=continente, pais=pais)
        return UbigeoProvincia.objects.filter(
            continente=continente, pais=pais, departamento=departamento)

    def provider_reniec(self):
        continente = get_object_or_404(
            UbigeoContinente,
            cod_ubigeo_reniec_continente=self.kwargs.get('cod_continente', ''))
        pais = get_object_or_404(
            UbigeoPais,
            cod_ubigeo_reniec_pais=self.kwargs.get('cod_pais', ''),
            continente=continente)
        departamento = get_object_or_404(
            UbigeoDepartamento,
            cod_ubigeo_reniec_departamento=self.kwargs.get('cod_departamento', ''),
            continente=continente, pais=pais)
        return UbigeoProvincia.objects.filter(
            continente=continente, pais=pais, departamento=departamento)


class ListaUbigeoDistritoAPI(ListAPIView):
    serializer_class = ListaUbigeoDistritoSerializer
    paginate_by = 100

    def get_queryset(self):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        continente = get_object_or_404(UbigeoContinente,
                                       cod_ubigeo_inei_continente=self.kwargs.get(
                                           'cod_continente', ''))
        pais = get_object_or_404(UbigeoPais,
                                 cod_ubigeo_inei_pais=self.kwargs.get(
                                     'cod_pais', ''),
                                 continente=continente)
        departamento = get_object_or_404(UbigeoDepartamento,
                                         cod_ubigeo_inei_departamento=self.kwargs.get(
                                             'cod_departamento', ''),
                                         continente=continente, pais=pais)
        provincia = get_object_or_404(UbigeoProvincia,
                                      cod_ubigeo_inei_provincia=self.kwargs.get(
                                          'cod_provincia', ''),
                                      continente=continente, pais=pais,
                                      departamento=departamento)

        return UbigeoDistrito.objects.filter(continente=continente, pais=pais,
                                             departamento=departamento,
                                             provincia=provincia)

    def provider_reniec(self):
        continente = get_object_or_404(UbigeoContinente,
                                       cod_ubigeo_reniec_continente=self.kwargs.get(
                                           'cod_continente', ''))
        pais = get_object_or_404(UbigeoPais,
                                 cod_ubigeo_reniec_pais=self.kwargs.get(
                                     'cod_pais', ''),
                                 continente=continente)
        departamento = get_object_or_404(UbigeoDepartamento,
                                         cod_ubigeo_reniec_departamento=self.kwargs.get(
                                             'cod_departamento', ''),
                                         continente=continente, pais=pais)
        provincia = get_object_or_404(UbigeoProvincia,
                                      cod_ubigeo_reniec_provincia=self.kwargs.get(
                                          'cod_provincia', ''),
                                      continente=continente, pais=pais,
                                      departamento=departamento)

        return UbigeoDistrito.objects.filter(continente=continente, pais=pais,
                                             departamento=departamento,
                                             provincia=provincia)


# -- Detalles
class DetalleUbigeoContinenteAPI(APIView):
    def get(self, request, format=None, **kwargs):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        obj = UbigeoContinente.objects.get(
            cod_ubigeo_inei_continente=self.kwargs.get('cod_continente'))
        serializer = DetalleUbigeoContinenteSerializer(obj, many=False)
        return Response(serializer.data)

    def provider_reniec(self):
        obj = UbigeoContinente.objects.get(
            cod_ubigeo_reniec_continente=self.kwargs.get('cod_continente'))
        serializer = DetalleUbigeoContinenteSerializer(obj, many=False)
        return Response(serializer.data)


class DetalleUbigeoPaisAPI(APIView):
    def get(self, request, format=None, **kwargs):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        obj = UbigeoPais.objects.get(
            continente__cod_ubigeo_inei_continente=self.kwargs.get(
                'cod_continente'),
            cod_ubigeo_inei_pais=self.kwargs.get('cod_pais'))
        serializer = DetalleUbigeoPaisSerializer(obj, many=False)
        return Response(serializer.data)

    def provider_reniec(self):
        obj = UbigeoPais.objects.get(
            continente__cod_ubigeo_reniec_continente=self.kwargs.get(
                'cod_continente'),
            cod_ubigeo_reniec_pais=self.kwargs.get('cod_pais'))
        serializer = DetalleUbigeoPaisSerializer(obj, many=False)
        return Response(serializer.data)


class DetalleUbigeoDepartamentoAPI(APIView):
    def get(self, request, format=None, **kwargs):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        departamento = UbigeoDepartamento.objects.get(
            continente__cod_ubigeo_inei_continente=self.kwargs.get(
                'cod_continente'),
            pais__cod_ubigeo_inei_pais=self.kwargs.get('cod_pais'),
            cod_ubigeo_inei_departamento=self.kwargs.get('cod_departamento'))
        serializer = DetalleUbigeoDepartamentoSerializer(departamento,
                                                         many=False)
        return Response(serializer.data)

    def provider_reniec(self):
        departamento = UbigeoDepartamento.objects.get(
            continente__cod_ubigeo_reniec_continente=self.kwargs.get(
                'cod_continente'),
            pais__cod_ubigeo_reniec_pais=self.kwargs.get('cod_pais'),
            cod_ubigeo_reniec_departamento=self.kwargs.get('cod_departamento'))
        serializer = DetalleUbigeoDepartamentoSerializer(departamento,
                                                         many=False)
        return Response(serializer.data)


class DetalleUbigeoProvinciaAPI(APIView):
    def get(self, request, format=None, **kwargs):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        obj = UbigeoProvincia.objects.get(
            continente__cod_ubigeo_inei_continente=self.kwargs.get(
                'cod_continente'),
            pais__cod_ubigeo_inei_pais=self.kwargs.get('cod_pais'),
            departamento__cod_ubigeo_inei_departamento=self.kwargs.get(
                'cod_departamento'),
            cod_ubigeo_inei_provincia=self.kwargs.get('cod_provincia'))
        serializer = DetalleUbigeoProvinciaSerializer(obj, many=False)
        return Response(serializer.data)

    def provider_reniec(self):
        obj = UbigeoProvincia.objects.get(
            continente__cod_ubigeo_reniec_continente=self.kwargs.get(
                'cod_continente'),
            pais__cod_ubigeo_reniec_pais=self.kwargs.get('cod_pais'),
            departamento__cod_ubigeo_reniec_departamento=self.kwargs.get(
                'cod_departamento'),
            cod_ubigeo_reniec_provincia=self.kwargs.get('cod_provincia'))
        serializer = DetalleUbigeoProvinciaSerializer(obj, many=False)
        return Response(serializer.data)


class DetalleUbigeoDistritoAPI(APIView):
    def get(self, request, format=None, **kwargs):
        if self.request.GET.get('provider', 'inei').lower() == 'inei':
            return self.provider_inei()
        else:
            return self.provider_reniec()

    def provider_inei(self):
        obj = UbigeoDistrito.objects.get(
            continente__cod_ubigeo_inei_continente=self.kwargs.get(
                'cod_continente'),
            pais__cod_ubigeo_inei_pais=self.kwargs.get('cod_pais'),
            departamento__cod_ubigeo_inei_departamento=self.kwargs.get(
                'cod_departamento'),
            provincia__cod_ubigeo_inei_provincia=self.kwargs.get(
                'cod_provincia'),
            cod_ubigeo_inei_distrito=self.kwargs.get('cod_distrito'))
        serializer = DetalleUbigeoDistritoSerializer(obj, many=False)
        return Response(serializer.data)

    def provider_reniec(self):
        obj = UbigeoDistrito.objects.get(
            continente__cod_ubigeo_reniec_continente=self.kwargs.get(
                'cod_continente'),
            pais__cod_ubigeo_reniec_pais=self.kwargs.get('cod_pais'),
            departamento__cod_ubigeo_reniec_departamento=self.kwargs.get(
                'cod_departamento'),
            provincia__cod_ubigeo_reniec_provincia=self.kwargs.get(
                'cod_provincia'),
            cod_ubigeo_reniec_distrito=self.kwargs.get('cod_distrito'))
        serializer = DetalleUbigeoDistritoSerializer(obj, many=False)
        return Response(serializer.data)
