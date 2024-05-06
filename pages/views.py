from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    """Renders the homepage"""
    template_name = 'home.html'

class AboutPageView(TemplateView):
    """Renders the about page"""
    template_name = 'about.html'
