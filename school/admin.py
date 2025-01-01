from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from school.models import (
    Banner,
    Teacher,
    Course,
    Videos,
    SocialActivity,
    DiscountItem,
    Contact,
    Main,
    News,
    ActivityImage

)
# Register your models here.




class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    min_num = 3
    extra = 0

class SocialActivityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['name']
    inlines = [ActivityImageInline]
admin.site.register(SocialActivity, SocialActivityAdmin)


admin.site.register(Banner)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(DiscountItem)
admin.site.register(Contact)
admin.site.register(Main)
admin.site.register(News)