from django.shortcuts import render

site_name = "Stylus photography"

def home_view(request):
    # database request
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'home.html', context)


def services_view(request):
    # database request
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'services.html', context)


def about_view(request):
    # database request
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'about.html', context)


def contact_view(request):
    # database request
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'contact.html', context)


def gallery_view(request):
    # database request
    context = {
        "site_name": site_name,
        "site_subtitle": "Ha már unod az egyforma képeket..."
    }

    return render(request, 'gallery.html', context)






