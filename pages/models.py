from django.db import models


class SiteInfo(models.Model):
    site_name = models.CharField("Oldalnév", max_length=200)  # kötelezően kitöltendő mező
    subtitle = models.CharField("Alcím", max_length=200)  # kötelezően kitöltendő mező
    email = models.EmailField("Email", max_length=200, blank=True)  # opcionálisan kitöltendő mező
    phone = models.CharField("Telefon", max_length=200, blank=True)  # opcionálisan kitöltendő mező

    class Meta:
        verbose_name_plural = "Oldal adatok"  # admin felületen a PAGES részben lévő adat neve ( lényegében a jelen osztály nevét írjuk így felül megjelenítéskor)

    def __str__(self):
        return self.site_name

