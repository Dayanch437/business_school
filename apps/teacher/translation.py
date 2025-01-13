from modeltranslation.translator import TranslationOptions, register
from .models import Teacher


@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'surname',
        'description',
        'major',
    )

