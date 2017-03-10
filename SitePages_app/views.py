from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_Base(request):
    return render(request, "SitePages/base.html")

def get_home(reguest):
    return render(reguest, "SitePages/home.html")

def get_about(request):
    return render(request, "SitePages/about.html")

def get_contact(request):
    return render(request, "SitePages/contact.html")
