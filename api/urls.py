from django.urls import path, include


urlpatterns = [
    path('school/',include('api.school.urls')),
]


