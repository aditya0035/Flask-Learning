from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def index(request):
    return render(request,"index.htm")

def sigin(request):
    form=forms.LoginForm()
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(username,password)
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    print("userauthenticated")
                    login(request,user)
                    return redirect("UserAuthentication:protectedMethod")
    return render(request,"UserAuthenticationApp/Login.htm",context={"form":form})

def register(request):
    userform=forms.UserForm()
    userportfolio=forms.UserPortFolioInfoForm()
    if request.method=='POST':
        userform=forms.UserForm(request.POST)
        userportfolio=forms.UserPortFolioInfoForm(request.POST)
        if userform.is_valid():
            user=userform.save(commit=False)
            user.set_password(user.password)
            print("user saved"+user.password)
            user.save()
            #user.set_paasword(user.password)
            if userportfolio.is_valid():
                userportfolioobj = userportfolio.save(commit=False)
                userportfolioobj.user=user
                if 'profilePhoto' in request.FILES:
                    userportfolioobj.profilePhoto=request.FILES['profilePhoto']
                userportfolioobj.save()
            else:
                print(userform.errors,userportfolio.errors)
    return render(request,"UserAuthenticationApp/Register.htm",context={"userform":userform,"userportfolio":userportfolio})
@login_required
def protectedMethod(request):
    return render(request,"UserAuthenticationApp/Protected.htm")
@login_required
def SignOut(request):
    logout(request)
    return redirect("UserAuthentication:index")

