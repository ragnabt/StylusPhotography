from django.db import models
from PIL import Image
from django.db.models.signals import post_delete, pre_save, post_save
import os

class SiteInfo(models.Model):
    site_name = models.CharField("Oldalnév", max_length=200)                # kötelezően kitöltendő mező
    logo = models.ImageField("Logo", upload_to="logo", blank=True)    # megadom a kép nevét és a mentés helyét...
    subtitle = models.CharField("Alcím", max_length=200)                    # kötelezően kitöltendő mező
    email = models.EmailField("Email", max_length=200, blank=True)          # opcionálisan kitöltendő mező
    phone = models.CharField("Telefon", max_length=200, blank=True)         # opcionálisan kitöltendő mező

    def save(self, *args, **kwargs):
        # if photo is being replaces
        self.replace_image()

        super(SiteInfo, self).save(*args, **kwargs)

        # resize uploded photo
        self.resize_image()

    def replace_image(self):
        try:
            site_info = SiteInfo.objects.get(id=self.id)
            if site_info.logo.name != self.logo.name:
                site_info.logo.delete(save=False)
            # site_info.logo.delete(save=False)

        except:
            pass

    def resize_image(self):
        image_path = self.logo.path
        img = Image.open(image_path)
        max_size = 300

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)



    class Meta:
        verbose_name_plural = "Oldal adatok"                                # admin felületen a PAGES részben lévő adat neve ( lényegében a jelen osztály nevét írjuk így felül megjelenítéskor)

    def __str__(self):
        return self.site_name


def logo_cleanup(sender, instance, **kwargs):  # törli az adatokkal együtt a feltöltött fájlokat is, ez esetben a logo-t
    os.remove(instance.logo.path)

post_delete.connect(logo_cleanup, sender=SiteInfo)



