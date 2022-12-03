from django.shortcuts import render

# Create your views here.

class Inicio(TemplateView):
    template_name = 'base.html'