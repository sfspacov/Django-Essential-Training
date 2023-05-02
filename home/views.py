from datetime import date
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name='home/welcome.html'
    extra_context = {'today': date.today()}

class AuthorizedView(TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'