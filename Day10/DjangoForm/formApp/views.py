from django.shortcuts import render
from .forms import UserForm
# Create your views here.
def index(request):
    return render(request,"index.htm")

def simpleform(request):
    user=UserForm()
    if request.method=="POST":
        user=UserForm(request.POST)
        is_valid=user.is_valid()
    return render(request,"formapp/simpleform.htm",context={"form":user})