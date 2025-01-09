
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
    Content,
    BigCart,
    SmallCart,
    CartImage
)


admin.site.register(CartImage)

class SmallCartInline(admin.TabularInline):
    model = SmallCart  # Use the SmallCart model
    extra = 1  # Number of blank forms to show for adding new SmallCart objects
    fields = ('title', 'description', 'image')  # Fields to display and edit in the inline
    show_change_link = True  # Add a link to edit the object in detail view

# Inline for BigCart objects
class BigCartInline(admin.TabularInline):
    model = BigCart  # Use the BigCart model
    extra = 1
    fields = ('title', 'description', 'image')
    show_change_link = True

# SocialActivity admin with inlines for related SmallCart and BigCart
@admin.register(SocialActivity)
class SocialActivityAdmin(admin.ModelAdmin):
    list_display = ('id',)  # Adjust fields to display for SocialActivity
    inlines = [SmallCartInline, BigCartInline]  # Add inlines for SmallCart and BigCart

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
    fields = ['images', 'title','description']
