from .models import SiteInfo

def global_context(request):
    site_infos = SiteInfo.objects.all()

    if not site_infos:
        return {}

    return {
        "site_name": site_infos[0].site_name,
        "logo": site_infos[0].image,
        "site_subtitle": site_infos[0].subtitle,
        "email": site_infos[0].email,
        "phone": site_infos[0].phone,

    }










