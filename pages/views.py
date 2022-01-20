from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, "home.html", {})

def genderGap(request):
    return render(request, "gendergap.html", {})

def aboutUs(request):
    return render(request, "aboutus.html", {})

