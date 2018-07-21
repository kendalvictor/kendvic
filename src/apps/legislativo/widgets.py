from dal import autocomplete

from .models import Laws


class LawsAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Laws.objects.all()

        if self.q:
            qs = qs.filter(tittle__iregex=self.q)

        return qs