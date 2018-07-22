from django.shortcuts import render
from dal import autocomplete
from django.http import Http404, HttpResponse, JsonResponse
from .models import Laws


class LawsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Laws.objects.all()

        if self.q:
            qs = qs.filter(tittle__iregex=self.q)

        return qs


def get_laws(request):
    data = {'data': []}
    error, status = '', 200
    try:
        data['data'] = [
            list(_) for _ in Laws.objects.all().order_by('-published').values_list(
                'code', 'tittle', 'status__name', 'comision__name', 'published',
                'like', 'comments')
        ]
    except Exception as e:
        error = str(e)
        status = 500

    return JsonResponse(data, status=status, reason=error, safe=False)
