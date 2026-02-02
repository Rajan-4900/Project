from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app4(request):
    return HttpResponse("This Is App4 Web Page")