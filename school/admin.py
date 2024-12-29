from django.contrib import admin
from school.models import (
    Banner,
    Teacher,
    Course,
    Videos,
    SocialActivity,
    DiscountItem,
    Contact,
    Main,
    MainText,
    Advise,

)
# Register your models here.

admin.site.register(Banner)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(SocialActivity)
admin.site.register(DiscountItem)
admin.site.register(Contact)
admin.site.register(Main)
admin.site.register(MainText)
admin.site.register(Advise)
