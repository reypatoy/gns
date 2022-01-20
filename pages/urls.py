from django.urls import path


from . import views

app_name = "pages"


urlpatterns = [
    path("", views.home_view, name="home"),
    path("GenderGap/", views.genderGap, name="genderGap"),
    path("AboutUs/", views.aboutUs, name="aboutUs"),
]
