from django.shortcuts import render
from django.views.generic import TemplateView

class home(TemplateView):
    template_name = 'home.html'

class about(TemplateView):
    template_name = 'about.html'