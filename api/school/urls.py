from rest_framework.routers import DefaultRouter

from .viewsets import (
    BannerViewSet,
    TeacherViewSet,
    CourseViewSet,
    VideoViewSet,
    DiscountItemViewSet,
    ContactViewSet,
    MainViewSet,
    NewsViewSet,
    SocialActivityViewSet
)


router = DefaultRouter()
urlpatterns = []

router.register('banner', BannerViewSet)
router.register('teacher', TeacherViewSet)
router.register('course', CourseViewSet)
router.register('video', VideoViewSet)
router.register('discount_item', DiscountItemViewSet)
router.register('contacts', ContactViewSet)
router.register('news', NewsViewSet)
router.register('main', MainViewSet,basename='main')
router.register('social_activity', SocialActivityViewSet)
urlpatterns += router.urls