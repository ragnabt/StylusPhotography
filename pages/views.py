from django.shortcuts import render

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
    # # database request
    # context = {
    #     "site_name": site_name,
    #     "site_subtitle": "Ha már unod az egyforma képeket..."
    # }

    # return render(request, 'services.html', context)
    return render(request, 'services.html')


def about_view(request):
    # # database request
    # context = {
    #     "site_name": site_name,
    #     "site_subtitle": "Ha már unod az egyforma képeket..."
    # }

    # return render(request, 'about.html', context)
    return render(request, 'about.html')


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






