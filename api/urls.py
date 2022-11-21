from django.urls import path, include
from . import views

app_name = "api"

urlpatterns = [
    path("sms/", views.sms, name="sms"),
    path("emails/", views.email, name="email"),
]
