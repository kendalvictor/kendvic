from django.conf.urls import url
from apps.legislativo.views import LawsAutocomplete
from . import views

urlpatterns = [
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^register/$',
        views.RegisterView.as_view(),
        name='register'),

    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^profile/$',
        views.ProfileView.as_view(),
        name='profile'),

    url(r'^ley-list/$',
        views.LeyListView.as_view(),
        name='ley-list'),

    url(r'^ley-list-post/$',
        views.LeyListPostView.as_view(),
        name='ley-list-post'),

    url(r'^analisis-twiter/$',
        views.AnalisisTwiterView.as_view(),
        name='analisis-twiter'),

    url(r'^reporte/$',
        views.ReporteView.as_view(),
        name='reporte'),

    url(
        r'^law-autocomplete/$',
        LawsAutocomplete.as_view(),
        name='law-autocomplete',
    ),
]
