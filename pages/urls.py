from django.urls import path

from .views import HomeView, AboutView, ContactView, ServicesView, ContactSentView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact', ContactView.as_view(), name="contact"),
    path('contact_sent/', ContactSentView.as_view(), name="contact_sent"),
    path('services', ServicesView.as_view(), name="services"),

]














