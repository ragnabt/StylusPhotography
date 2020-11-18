from django.shortcuts import render
from .models import About, Services

# context = {
#         "site_name": "Stylus photography",
#         "site_subtitle": "Ha már unod az egyforma képeket..."
#     }

def home_view(request):
    # # database request
    # context = {
    #     "site_name": "Stylus photography",
    #     "site_subtitle": "Ha már unod az egyforma képeket..."
    # }

    # return render(request, 'home.html', context)
    return render(request, 'home.html')


def services_view(request):
    services = Services.objects.all()
    context = {
        "services" : services
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


def gallery_view(request):

    return render(request, 'gallery.html')






