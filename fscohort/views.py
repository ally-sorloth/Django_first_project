from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Hi, this is a home page in fscohort view</h1>")


def home_about(request):
    return HttpResponse("<h1>Hi, this is fscohort in about page</h1>")