from modeltranslation.translator import TranslationOptions,register
from .models import Main


@register(Main)
class MainTranslationOptions(TranslationOptions):v
    fields = ['title','description']

