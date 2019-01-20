from django.urls import path
from . import views
app_name="ModelFormApp"
urlpatterns = [
    path("",views.index, name="index"),
    path("form",views.simpleform, name="form")
]
