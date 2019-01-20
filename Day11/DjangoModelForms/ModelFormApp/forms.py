from django import forms
from  . import models
class CustomForm(forms.ModelForm):

    class Meta:
        model=models.CustomModel
        #fields="__all__" #all fields goes here 
        fields=("lastName","firstName",'username') #included fields
        #exclude("username","firstname") #these fields will be excluded
    def clean(self):
        dictOfValue=super().clean()
        print(dictOfValue)