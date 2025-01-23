from modeltranslation.translator import TranslationOptions,register

from apps.socialactivity.models import SocialActivity





@register(SocialActivity)
class SocialActivityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
