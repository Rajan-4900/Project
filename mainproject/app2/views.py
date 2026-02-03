from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


# def app2(request):
#     return HttpResponse("This Is App2 Web Page")

def cards(request):
 return render(request,"cards.html")