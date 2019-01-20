from django.shortcuts import render,redirect
from .models import UserData
# Create your views here.

def index(request):
    userdata=UserData.objects.all()
    print(userdata)
    return render(request,"index.htm",context={"userdata":userdata})

def simpleform(request):
    if request.method=="POST":
        print(request.POST)
        firstName=request.POST["firstName"]
        lastName=request.POST["lastName"]
        userdata=UserData(firstName=firstName,lastName=lastName)
        userdata.save()
        return redirect("index")
    return render(request,"formsCollections/SimplePostForm.htm")