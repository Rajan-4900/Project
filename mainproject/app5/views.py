from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app5(request):
    return HttpResponse("This Is App5 Web Page")