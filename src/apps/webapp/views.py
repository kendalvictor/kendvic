from django.shortcuts import render
from .forms import LawHomeForm
# Create your views here.
from django.views.generic import TemplateView, FormView


class HomeView(FormView):
    form_class = LawHomeForm
    template_name = 'index.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class LeyListView(TemplateView):
    template_name = 'ley_list.html'


class LeyListPostView(TemplateView):
    template_name = 'ley_list_post.html'


class AnalisisTwiterView(TemplateView):
    template_name = 'twiter.html'
