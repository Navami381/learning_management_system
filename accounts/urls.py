from django.urls import path
from accounts.views import AdminCreateView,StudentCreateView
from accounts.views import ProfileUpdateView,ProfileMeView,ObtainAuthToken
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns=[
    path("admin/register/",AdminCreateView.as_view()),
    path("student/register/",StudentCreateView.as_view()),
    path("profile/complete/",ProfileUpdateView.as_view()),
    path("profile/me/",ProfileMeView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("jwt/token/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),
]