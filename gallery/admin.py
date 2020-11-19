from django.contrib import admin
from .models import Category, Photo

admin.site.register(Category)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "uploaded", "image"]
    list_editable = ["category"]
    search_fields = ["title"]
    list_filter = ["category"]


admin.site.register(Photo, PhotoAdmin)



