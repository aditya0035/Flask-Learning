from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def index(request):
    alldata=models.CustomModel.objects.all()
    return render(request,"index.htm",context={'data':alldata})

def simpleform(request):
    customForm=forms.CustomForm()
    if request.method=='POST':
        customForm=forms.CustomForm(request.POST)
        if customForm.is_valid():
            customForm.save()
            return redirect("ModelFormApp:index")
    return render(request,"ModelForm/form.htm",context={"form":customForm})