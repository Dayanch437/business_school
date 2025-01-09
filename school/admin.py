
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
    Image,
    Content
)

#
# class ActivityImageInline(admin.TabularInline):
#     model = ActivityImage
#     min_num = 3
#     extra = 0

# class SocialActivityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
#     list_display = ['name']
#     inlines = [ActivityImageInline]
# admin.site.register(SocialActivity, SocialActivityAdmin)
#



admin.site.register(Banner)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(DiscountItem)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Image)
admin.site.register(Content)


@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    model = Main
    fields = ['images', 'content']
