from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,template_name="listings/index.html")

def listing(request):
    return render(request,template_name="listings/listing.html")

def search(request):
    return render(request,template_name="listing/search.html")
