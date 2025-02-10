from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.school.models import Main
from apps.discount.models import DiscountItem
from apps.course.models import Course
from apps.socialactivity.models import SocialActivity,Image
from apps.video.models import Videos
from apps.teacher.models import Teacher
from apps.news.models import News
from apps.contact.models import Contact
from apps.banner.models import Banner



admin.site.register(Banner,ImportExportModelAdmin)
admin.site.register(Teacher,ImportExportModelAdmin)
admin.site.register(Course,ImportExportModelAdmin)
admin.site.register(Videos,ImportExportModelAdmin)
admin.site.register(DiscountItem,ImportExportModelAdmin)
admin.site.register(Contact,ImportExportModelAdmin)
admin.site.register(News,ImportExportModelAdmin)
admin.site.register(Main,ImportExportModelAdmin)
