from modeltranslation.translator import translator, TranslationOptions,register
from .models import Course





@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name','description')