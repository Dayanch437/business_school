from django.db import models

# Create your models here.


class DiscountItem(models.Model):
    description = models.CharField(max_length=255)
    percentage = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'discount item'
        verbose_name_plural = 'discount items'
    def __str__(self):
        return f"{self.description}"

