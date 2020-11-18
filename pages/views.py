from django.shortcuts import render
from .models import About, Services, Home

# context = {
#         "site_name": "Stylus photography",
#         "site_subtitle": "Ha már unod az egyforma képeket..."
#     }


def home_view(request):
    home = Home.objects.all()
    context = {}

    if home:
        context = {
            "home": home[0]
        }
    return render(request, 'home.html', context)


def services_view(request):
    services = Services.objects.order_by('title')
    for i in services:
        print(i.title)
    context = {
        "services": services
    }
    return render(request, 'services.html', context)


def about_view(request):
    abouts = About.objects.all()
    context = {}
    if abouts:
        context["title"] = abouts[0].title
        context["content"] = abouts[0].content

    return render(request, 'about.html', context)


def contact_view(request):
    # # database request
    # context = {
    #     "site_name": site_name,
    #     "site_subtitle": "Ha már unod az egyforma képeket..."
    # }

    # return render(request, 'contact.html', context)
    return render(request, 'contact.html')









