from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf.urls.static import static


urlpatterns = []


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path(
        'panel/admin/',
        admin.site.urls
    ),
    path(
        'api-auth/',
        include('rest_framework.urls')
    ),
    path(
        'legislativo/',
        include('apps.legislativo.urls')
    ),
    path(
        '',
        include('apps.webapp.urls')
    ),
    path(
        '',
        RedirectView.as_view(
            url='portada/',
            permanent=False
        ),
        name='portada'
    ),

]
