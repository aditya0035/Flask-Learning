from django.shortcuts import render
from .models import Listing
# Create your views here.

def index(request):
    #listings=Listing.objects.all()
    listings=None
    osql=Listing.objects
    where=request.GET.get('where',None)
    if where is not None:
        osql.filter_by(where)
    top=request.GET.get('top',None)
    print(top)
    listings=osql.all()
    if top is not None:
        listings=listings[:int(top)]
    context={"listings":listings}
    return render(request,template_name="listings/index.htm",context=context)

def listing(request,listing_id):
    return render(request,template_name="listings/listing.html")

def search(request):
    return render(request,template_name="listing/search.html")
