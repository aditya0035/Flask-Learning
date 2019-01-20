from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display=('id','title','description','price','realtors')
    list_display_links=('title',)
    list_filter=('realtors','title')
    list_editable=('realtors',)
    search_fields=('title','price')
    list_perpage=25

admin.site.register(Listing,ListingAdmin)
