import csv
import re

import tweepy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import RedirectView
from django.views.generic import TemplateView, FormView
from textblob import TextBlob

from apps.legislativo.models import Laws
from . import forms
from .forms import LawHomeForm, TwiterForm


class HomeView(FormView):
    form_class = LawHomeForm
    template_name = 'index.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class ProfileView(TemplateView):
    template_name = 'profile.html'


class LeyListView(TemplateView):
    template_name = 'ley_list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        order = request.GET.get('order', '')
        laws = Laws.objects.all()
        try:
            context['list_laws'] = laws.order_by('-' + order)[:10]
        except:
            context['list_laws'] = laws.order_by('-published')[:10]

        return self.render_to_response(context)


class LeyListPostView(TemplateView):
    template_name = 'ley_list_post.html'


class ReporteView(TemplateView):
    template_name = 'reporte.html'


class AnalisisTwiterView(TemplateView):
    template_name = 'twiter.html'

    def get(self, request, *args, **kwargs):
        self.twiter_form = TwiterForm()
        self.result = False
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        twiter = request.POST.get("twiter")
        self.twiter_form = TwiterForm(request.POST)
        if twiter:

            consumer_key = 'OoKtdnkn2PhPdVopgcPPVszBL'
            consumer_secret = 'zJCI08nnQ7wGiosCOe7Udbu4PlpchanXFbjytZZJFkontr2wOC'

            access_token = '572213920-pfExxBDxG4W7gu6ke8Yh1xexYcypE9QOddfvpY6u'
            access_token_secret = 'C2tOsrGpF48uBoxVjcyHYptljLpfAesln2ABZacpLy1mL'

            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)

            query = twiter
            public_tweets = api.search(query, count=5)

            def clean_tweet(tweet):
                tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
                return tweet

            def run(public_tweets):
                positive2 = 0
                negative2 = 0
                neutro2 = 0
                _public_tweets = list()
                for tweet in public_tweets:
                    cleaned_tweet = clean_tweet(tweet.text)
                    from aylienapiclient import textapi
                    client = textapi.Client("5c6fcdc1", "e40ab9593487f13430af2283d2f2e09c")
                    sentiment = client.Sentiment({'text': '{0}'.format(cleaned_tweet)})

                    if str(sentiment["polarity"]) == "positive":
                        positive2 += 1
                    elif str(sentiment["polarity"]) == "negative":
                        negative2 += 1
                    else:
                        neutro2 += 1
                    _public_tweets.append([cleaned_tweet, sentiment["polarity"]])

                my_total = positive2 + negative2 + neutro2
                rs = dict(positive=positive2, negative=negative2,
                          neutrive=neutro2, public_tweets=_public_tweets,
                          cantidad=my_total)
                return rs

            datos = run(public_tweets)
            self.positivo = datos["positive"]
            self.negativo = datos["negative"]
            self.neutrive = datos["neutrive"]
            self.total = datos["cantidad"]
            self.public_tweets = datos["public_tweets"]
            self.result = True
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["twiter_form"] = self.twiter_form
        if self.result:
            context["positivo"] = self.positivo
            context["negativo"] = self.negativo
            context["neutrive"] = self.neutrive
            context["public_tweets"] = self.public_tweets
            context["total"] = self.total
        return context


class LoginView(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm

    def form_valid(self, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        next = self.request.GET.get('next')
        if next is not None:
            return next
        return '/'


class LogoutView(RedirectView):

    def get_redirect_url(self, **kwargs):
        logout(self.request)
        self.request.session.flush()
        return '/'
