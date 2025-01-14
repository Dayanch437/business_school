from modeltranslation.translator import register, TranslationOptions
from .models import News

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # Fields you want to translate
