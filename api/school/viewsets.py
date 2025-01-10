from drf_spectacular.utils import extend_schema,OpenApiResponse
from django.core.cache import cache
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status



from apps.school.models import (
    Teacher,
    Course,
    DiscountItem,
    Videos,
    Contact,
    Main,
    SocialActivity
)
from apps.news.models import News
from apps.banner.models import Banner


from .serializer import (
    BannerSerializer,
    TeacherSerializer,
    CourseSerializer,
    VideoSerializer,
    DiscountItemSerializer,
    ContactSerializer,
    ContactVerificationSerializer,
    MainSerializer,
    NewsSerializer, SocialActivitySerializer

)


@extend_schema(
    tags=["Banner"],
    summary="Banner",
    responses=BannerSerializer,
)
class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer



@extend_schema(
    tags=["Teacher"],
    summary="Teacher",
    responses=TeacherSerializer,
)
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

@extend_schema(
    tags=["Course"],
    summary="Course",
    responses=CourseSerializer
)
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@extend_schema(
    tags=["Video"],
    summary="Video",
    responses=VideoSerializer)
class VideoViewSet(ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer




@extend_schema(
    tags=["Discount Item"],
    summary="Discount Item",
    responses= DiscountItemSerializer
)
class DiscountItemViewSet(ModelViewSet):
    queryset = DiscountItem.objects.all()
    serializer_class = DiscountItemSerializer




@extend_schema(
    tags=["Contact"],
    summary="ContactViewSet",
    responses=ContactSerializer,
)
class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']

    @extend_schema(
        summary="Create new comment",
        description="""Creates a new comment according provided datas {
                  "username": string,
                  "email": string,
                  "comment": string,
                    }""",
        request=ContactSerializer,
        responses={
            201: OpenApiResponse(description="Verification code was sent to provided email."),
            400: OpenApiResponse(description="Invalid datas you provided or check your internet connection."),
        },
    )

    def create(self, request, *args, **kwargs):
        """
        Sends a verification email to the provided email address.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Verification email sent. Please verify to complete."},
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        summary="Verify email with code",
        description="Verifies the provided email using the verification code sent earlier. Creates a contact if verification succeeds.",
        request=ContactVerificationSerializer,
        responses={
            201: OpenApiResponse(description="Email verified and contact saved successfully."),
            400: OpenApiResponse(description="Invalid or expired verification code."),
        },
    )

    @action(detail=False, methods=['post'], url_path='verify-email')
    def verify_email(self, request):

        serializer = ContactVerificationSerializer(data=request.data)

        if serializer.is_valid():
            gmail = serializer.validated_data['gmail']
            verification_code = serializer.validated_data['verification_code']

            cached_data = cache.get(f'verification_{gmail}')

            if cached_data and cached_data['code'] == verification_code:
                Contact.objects.create(
                    gmail=gmail,
                    username=cached_data['username'],
                    comment=cached_data['comment'],
                    is_verified=True,
                )

                cache.delete(f'verification_{gmail}')

                return Response(
                    {"message": "Email verified and contact saved successfully!"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": "Invalid or expired verification code."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=["Main"],
    summary="Main",
    responses= MainSerializer,
)
class MainViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer




@extend_schema(
     tags=["News"],
    summary="News",
    responses=NewsSerializer
)
class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema(
    tags=["SocialActivity"],
    summary="SocialActivity",
    responses= SocialActivitySerializer,
)
class SocialActivityViewSet(ModelViewSet):
    queryset = SocialActivity.objects.all()
    serializer_class = SocialActivitySerializer
    http_method_names = ['get']
