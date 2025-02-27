from modeltranslation.translator import register, TranslationOptions
from .models import Videos


@register(Videos)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)

