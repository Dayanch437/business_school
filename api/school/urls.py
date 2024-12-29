from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import (
    BannerViewSet,
    TeacherViewSet,
    CourseViewSet,
    VideoViewSet,
    SocialActivityViewSet,
    DiscountItemViewSet,
    ContactViewSet,
    Main,
    AdviseViewSet, MainViewSet,

)


router = DefaultRouter()
urlpatterns = []

router.register('banner', BannerViewSet)
router.register('teacher', TeacherViewSet)
router.register('course', CourseViewSet)
router.register('video', VideoViewSet)
router.register('social_activity', SocialActivityViewSet)
router.register('discount_item', DiscountItemViewSet)
router.register('contacts', ContactViewSet)

router.register('main', MainViewSet,basename='main')
router.register('advise', AdviseViewSet,basename='advise')





urlpatterns += router.urls