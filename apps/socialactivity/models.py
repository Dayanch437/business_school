from django.db import models
from util.utils import CompressedImageField

# Create your models here.

class CartImage(models.Model):
    image = CompressedImageField(upload_to='cartImages/',null=True,blank=True)
    def __str__(self):
        return self.image.name


class SocialActivity(models.Model):
    class Meta:
        verbose_name = 'social activity'
        verbose_name_plural = 'social activities'
        db_table = 'socialActivity'



class SmallCart(models.Model):
    social_activity = models.ForeignKey(SocialActivity, on_delete=models.CASCADE, related_name='small_carts')
    image = models.ManyToManyField(CartImage, related_name='small_cart')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'small cart'
        verbose_name_plural = 'small carts'
        db_table = 'smallCart'