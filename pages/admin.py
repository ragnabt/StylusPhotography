from django.contrib import admin

# Register your models here.

from .models import SiteInfo
admin.site.register(SiteInfo)
