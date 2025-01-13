from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.school.models import Main
from apps.discount.models import DiscountItem
from apps.course.models import Course
from apps.socialactivity.models import SocialActivity,SmallCart,CartImage
from apps.video.models import Videos
from apps.teacher.models import Teacher
from apps.news.models import News
from apps.contact.models import Contact
from apps.banner.models import Banner
from modeltranslation.admin import TranslationTabularInline,TranslationStackedInline



class SmallCartInline(TranslationStackedInline):
    model = SmallCart  # Use the SmallCart model
    extra = 0  # Number of blank forms to show for adding new SmallCart objects
    fields = ('title', 'description', 'image')  # Fields to display and edit in the inline
    show_change_link = True  # Add a link to edit the object in detail view

@admin.register(SocialActivity)
class SocialActivityAdmin(admin.ModelAdmin):
    list_display = ('id',)  # Adjust fields to display for SocialActivity
    inlines = [SmallCartInline]  # Add inlines for SmallCart and BigCart

admin.site.register(Banner,ImportExportModelAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(DiscountItem)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Main)
admin.site.register(CartImage)
