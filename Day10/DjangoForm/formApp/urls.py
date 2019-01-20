from django.urls import path
from . import views
app_name ='formApp'
urlpatterns = [
    path("",views.index,name="index"),
    path("form",views.simpleform,name="form")
]
