from django.shortcuts import render
from .forms import LawHomeForm, TwiterForm
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

    def get(self, request, *args, **kwargs):
        self.twiter_form = TwiterForm()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        establecimiento = request.POST.get("establecimiento")
        if establecimiento:
            self.request.session['actual_establecimiento'] = establecimiento
            return redirect('paciente-app:admision:list')
        else:
            return redirect('paciente-app:establecimiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["twiter_form"] = self.twiter_form
        return context
