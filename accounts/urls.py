from django.urls import path
from accounts.views import AdminCreateView


urlpatterns=[
    path("admin/register/",AdminCreateView.as_view())
]