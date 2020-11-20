
from django.views.generic import ListView, DetailView
from .models import Photo, Category


class GalleryView(ListView):
    model = Photo
    template_name = "gallery/gallery_home.html"
    context_object_name = "photos"

    extra_context = {
        "categories": Category.objects.order_by("title")

    }


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "gallery/photo_details.html"
    context_object_name = "photo"
