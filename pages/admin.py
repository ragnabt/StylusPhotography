from django.contrib import admin

# Register your models here.

from .models import SiteInfo, About, Services, Home

admin.site.register(Home)
admin.site.register(SiteInfo)
admin.site.register(About)
admin.site.register(Services)



