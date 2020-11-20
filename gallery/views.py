
from django.views.generic import ListView, DetailView
from .models import Photo, Category


class GalleryView(ListView):
    model = Photo
    template_name = "gallery/gallery_home.html"
    context_object_name = "photos"

    extra_context = {
        "categories": Category.objects.order_by("title")
    }

    def get_queryset(self):
        photos = Photo.objects.order_by('-uploaded')
        category_name = self.request.GET.get("category")

        if category_name:
            photos = Photo.objects.filter(category__title=category_name)
            photos = photos.order_by('-uploaded')

        print(category_name)

        return photos


class PhotoDetailView(DetailView):
    model = Photo
    template_name = "gallery/photo_details.html"
    context_object_name = "photo"
