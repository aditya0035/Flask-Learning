
from django.template import loader 
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,template_name="pages/index.html")

def about(request):
    template=loader.get_template(template_name= "pages/about.html")
    return HttpResponse(template.render(context=None,request=request))
