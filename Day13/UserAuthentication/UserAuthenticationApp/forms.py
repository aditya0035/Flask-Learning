from django import forms
from django.contrib.auth.admin import User
from .models import UserPortFolioInfo
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        exclude=('last_login','is_superuser','id_groups','user_permissions','is_staff','date_joined','groups',)


class UserPortFolioInfoForm(forms.ModelForm):
    class Meta:
        model=UserPortFolioInfo
        exclude=('user',)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput)
    # class Meta:
    #     model=User
    #     fields=("username","password")

