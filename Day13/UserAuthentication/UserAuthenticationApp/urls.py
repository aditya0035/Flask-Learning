from django.urls import path
from . import views
app_name="UserAuthentication"
urlpatterns = [
    path("",views.index,name="index"),
    path("register",views.register,name="register"),
    path("login",views.sigin,name="login"),
    path("logout",views.SignOut,name="signout"),
    path("details",views.protectedMethod,name="protectedMethod")
]
