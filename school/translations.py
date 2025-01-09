from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Banner,
    Teacher,
    Course,
    Videos,
    SocialActivity,
    DiscountItem,
    Contact,
    Main,

)


class BannerTranslationOptions(TranslationOptions):
    fields = ['title']
translator.register(Banner,BannerTranslationOptions)

class TeacherTranslationOptions(TranslationOptions):
    fields = ['name','surname','subject']
translator.register(Teacher,TeacherTranslationOptions)

class CourseTranslationOptions(TranslationOptions):
    fields = ['name','description','duration','price']
translator.register(Course,CourseTranslationOptions)

class VideoTranslationOptions(TranslationOptions):
    fields = ['title']
translator.register(Videos,VideoTranslationOptions)

class SocialActivityTranslationOptions(TranslationOptions):
    fields = ['name','description']
translator.register(SocialActivity,SocialActivityTranslationOptions)

class DiscountItemTranslationOptions(TranslationOptions):
    fields = ['description']
translator.register(DiscountItem,DiscountItemTranslationOptions)

class MainTranslationOptions(TranslationOptions):
    fields = ['title','description']
translator.register(Main,MainTranslationOptions)


