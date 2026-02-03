
from django.urls import path
from app1.views import index , about, contact ,projects


urlpatterns = [
    path("app1/", index, name='index'),
    path("app1/index.html", index, name='index'),
    path("app1/about.html", about, name='about'),
    path("app1/contact.html", contact, name='contact'),
    path("app1/projects.html", projects, name='projects'),
]