from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def index(request):
    template=loader.get_template(template_name="pages/index.htm")
    return HttpResponse(template.render(context=None,request=request))

def about(request):
    return render(request,template_name="pages/about.htm")