
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.school.models import (
    Teacher,
    Course,
    Videos,
    SocialActivity,
    DiscountItem,
    Contact,
    Main,
    Image,
    Content,
    SmallCart,
    CartImage
)


from apps.news.models import News
from apps.banner.models import Banner

admin.site.register(CartImage)

class SmallCartInline(admin.TabularInline):
    model = SmallCart  # Use the SmallCart model
    extra = 0  # Number of blank forms to show for adding new SmallCart objects
    fields = ('title', 'description', 'image')  # Fields to display and edit in the inline
    show_change_link = True  # Add a link to edit the object in detail view

#
# SocialActivity admin with inlines for related SmallCart and BigCart
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
admin.site.register(Image)
admin.site.register(Content)

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    model = Main
    fields = ['images', 'title','description']
