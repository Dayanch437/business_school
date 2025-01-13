from modeltranslation.translator import translator, TranslationOptions,register
from .models import SmallCart




@register(SmallCart)
class SmallCartTranslationOptions(TranslationOptions):
    fields = ['title','description']

