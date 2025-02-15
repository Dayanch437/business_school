from django.db import models

# Create your models here.


class FooterData(models.Model):
    name = models.CharField(max_length=100,default="Uznuksiz Bilim Merkezi")
    gmail = models.CharField("Gmail", max_length=255)
    phone = models.CharField("Phone", max_length=255)
    instagram = models.CharField("Instagram", max_length=255)
    tiktok = models.CharField("TikTok", max_length=255)

    class Meta:
        verbose_name = "FooterData"
        verbose_name_plural = "FooterData"

    def __str__(self):
        return self.name

