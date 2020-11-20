from django.urls import path

from .views import GalleryView, PhotoDetailView

urlpatterns = [
    path('', GalleryView.as_view(), name="gallery_home"),
    path('<str:slug>/', PhotoDetailView.as_view(), name="photo_details")
]