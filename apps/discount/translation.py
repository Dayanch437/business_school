from modeltranslation.translator import translator, TranslationOptions,register
from .models import DiscountItem



@register(DiscountItem)
class DiscountItemTranslationOptions(TranslationOptions):
    fields = ('description',)


