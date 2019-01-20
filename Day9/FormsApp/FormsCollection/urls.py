from django.urls import path
from .views import index,simpleform
urlpatterns = [
    path("",index,name="index"),
    path("simpleform",simpleform,name="simpleform")
]
