from django.db import models
from PIL import Image
from django.db.models.signals import post_delete, pre_save, post_save
import os


class SiteInfo(models.Model):
    site_name = models.CharField("Oldalnév", max_length=200)                # kötelezően kitöltendő mező
    image = models.ImageField("Logo", upload_to="logo", blank=True)    # megadom a kép nevét és a mentés helyét...
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
            if site_info.image.name != self.image.name:
                site_info.image.delete(save=False)
            # site_info.logo.delete(save=False)

        except:
            pass

    def resize_image(self):
        image_path = self.image.path
        img = Image.open(image_path)
        max_size = 300

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)



    class Meta:
        verbose_name_plural = "Oldal adatok"                                # admin felületen a PAGES részben lévő adat neve ( lényegében a jelen osztály nevét írjuk így felül megjelenítéskor)

    def __str__(self):
        return self.site_name


class About(models.Model):
    title = models.CharField('Címsor', max_length=200)
    content = models.TextField('Üzenet', max_length=5000)

    class Meta:
        verbose_name_plural = "Rólunk"                                # admin felületen a PAGES részben lévő adat neve ( lényegében a jelen osztály nevét írjuk így felül megjelenítéskor)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField('Cím', max_length=200)
    image = models.ImageField('Kép', upload_to='services')
    content = models.TextField('Leírás', max_length=5000)

    def save(self, *args, **kwargs):
        # if photo is being replaces
        self.replace_image()

        super().save(*args, **kwargs)

        # resize uploded photo
        self.resize_image()

    def replace_image(self):
        try:
            service_object = Services.objects.get(id=self.id)
            if service_object.image.name != self.image.name:
                service_object.image.delete(save=False)
            # site_info.logo.delete(save=False)

        except:
            pass

    def resize_image(self):
        image_path = self.image.path
        img = Image.open(image_path)
        max_size = 800

        if img.size[0] > max_size or img.size[1] > max_size:
            img.thumbnail((max_size, max_size))
            img.save(image_path)

    class Meta:
        verbose_name_plural = "Szolgáltatásaink"                                # admin felületen a PAGES részben lévő adat neve ( lényegében a jelen osztály nevét írjuk így felül megjelenítéskor)

    def __str__(self):
        return self.title


def image_cleanup(sender, instance, **kwargs):  # törli az adatokkal együtt a feltöltött fájlokat is, ez esetben a logo-t
    os.remove(instance.image.path)


post_delete.connect(image_cleanup, sender=SiteInfo)
post_delete.connect(image_cleanup, sender=Services)
