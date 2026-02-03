from django.urls import path
# from app2.views import app2 
from app2.views import  cards


urlpatterns = [
    # path("app2",app2,name='app2'),
    path("app2/", cards, name='cards'),

]
