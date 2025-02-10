from django.contrib import admin
from .models import Image,SocialActivity
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class ActivityImageInline(admin.TabularInline):
    model = Image
    min_num = 3
    extra = 0


class SocialActivityAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['title']
    inlines = [ActivityImageInline]
admin.site.register(SocialActivity, SocialActivityAdmin)

