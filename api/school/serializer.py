from rest_framework import serializers
from django.core.cache import cache
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string


from apps.school.models import  Main
from apps.socialactivity.models import SocialActivity,CartImage,SmallCart
from apps.course.models import Course
from apps.video.models import Videos
from apps.teacher.models import Teacher
from apps.news.models import News
from apps.banner.models import Banner
from apps.discount.models import DiscountItem




class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','title','image',"description"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','surname','description','image','major']



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','image','description','duration','price']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id','title','video','image',]


class DiscountItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountItem
        fields = ['id','description','percentage']


class ContactSerializer(serializers.Serializer):
    username = serializers.CharField()
    gmail = serializers.EmailField()
    comment = serializers.CharField()

    def save(self):
        verification_code = str(randint(100000, 999999))
        print(verification_code)
        gmail = self.validated_data['gmail']

        # Cache the verification data
        cache.set(
            f'verification_{gmail}',
            {
                'code': verification_code,
                'username': self.validated_data['username'],
                'comment': self.validated_data['comment'],
            },
            timeout=600,  # Cache timeout in seconds
        )
        code = verification_code
        current_time = datetime.now().year
        html_content = render_to_string(
            "emails/user_verification.html",
            {
                "code": code,
                "current_year": current_time,
            }
        )
        send_mail(
            'Email Verification Code',
            f'Your verification code is: {verification_code}',
            settings.DEFAULT_FROM_EMAIL,
            (gmail,),
            html_message=html_content,
            fail_silently=False,
        )

class ContactVerificationSerializer(serializers.Serializer):
    gmail = serializers.EmailField()
    verification_code = serializers.CharField(max_length=6)


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['title','description']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title','image','description','date']


class SmallCartSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, instance) -> list:
        return [image.image.url for image in instance.image.all()]

    class Meta:
        model = SmallCart
        fields = ['images', 'title', 'description', 'date']



class SocialActivitySerializer(serializers.ModelSerializer):
    small_carts = SmallCartSerializer(many=True)  # Use `related_name`

    class Meta:
        model = SocialActivity
        fields = ['small_carts']