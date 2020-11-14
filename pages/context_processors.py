from .models import SiteInfo

def global_context(request):
    site_infos = SiteInfo.objects.all()
    # print(site_infos[0].site_name)
    # print(site_infos[0].subtitle)
    # print(site_infos[0].email)
    # print(site_infos[0].phone)

    if not site_infos:
        return {}

    return {
        "site_name": site_infos[0].site_name,
        "site_subtitle": site_infos[0].subtitle,
        "email": site_infos[0].email,
        "phone": site_infos[0].phone,

    }










