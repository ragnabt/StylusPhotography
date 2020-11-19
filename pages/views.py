from django.shortcuts import render
from .models import About, Services, Home
from django.views.generic import TemplateView, ListView


class HomeView(TemplateView):
    template_name = "home.html"
    home = Home.objects.all()
    if Home:
        extra_context = {
            "home": home[0]
        }


class ServicesView(ListView):
    model = Services
    template_name = "services.html"
    context_object_name = "services"


class AboutView(TemplateView):
    template_name = "about.html"
    abouts = About.objects.all()
    if abouts:
        extra_context = {
            "about": abouts[0]
        }


class ContactView(TemplateView):
    template_name = "contact.html"






