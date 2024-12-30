from rest_framework import serializers
from django.core.cache import cache
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string

from school.models import (
    Banner,
    Teacher,
    Course,
    Videos,
    SocialActivity,
    ActivityImage,
    DiscountItem,
    Main,
    MainText,
    Advise, News
)



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','title','image',"description"]


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','surname','subject','image']



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','name','image','description','duration','price']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ['id','title','video','image',]

class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = ['id', 'image']

class SocialActivitySerializer(serializers.ModelSerializer):
    images = ActivityImageSerializer(many=True)
    class Meta:
        model = SocialActivity
        fields = ['id','name','description','images']

class DiscountItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountItem
        fields = ['id','description','percentage','image']


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

class MainTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainText
        fields = ['id','title','description']


class AdviseSerializer(serializers.ModelSerializer):
    leftside = MainTextSerializer()
    rightside = MainTextSerializer()
    class Meta:
        model = Advise
        fields = ['id','title','image','description','leftside','rightside']

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ['id','title','image','description']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','title','image','description','date']