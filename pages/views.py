from .models import About, Services, Home
from django.views.generic import TemplateView, ListView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail


class HomeView(TemplateView):
    template_name = 'home.html'
    home = Home.objects.all()
    if home:
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


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_sent")

    def form_valid(self, form):
        name = form.data["name"]
        email = form.data["email"]
        message = form.data["message"]

        send_mail(
            f'Üzenet: {name}',
            message,
            email,
            ['to@example.com'],
            fail_silently=False
        )

        return super().form_valid(form)


class ContactSentView(TemplateView):
    template_name = "email_sent.html"







