from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest


def home(request):
    return HttpResponse('Hello, World!')


def welcome(request):
    return render(request, "app1/welcome.html")

def another(request):
    return render(request, "app1/dynamic.html", {"name":"shivraj"})

def home1(request):
    return HttpResponse("hello dear")