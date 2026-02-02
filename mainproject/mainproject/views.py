from django.http import HttpResponse

def name(request):
    return HttpResponse("Rajan")

def contact(request):
    return HttpResponse("9184293898")

def email(request):
    return HttpResponse("rajan91480@gmail.com")

def home(request):
    return HttpResponse("Bangalore")

