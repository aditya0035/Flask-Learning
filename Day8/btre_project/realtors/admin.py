from django.contrib import admin
from .models import Realtor
# Register your models here.

class RealtorsAdmin(admin.ModelAdmin):
    list_display=('id','name','photo','description','email','phone')
    list_display_link=('name',)
    list_filter=('name',)
    list_editable=('phone',)
    search_fields=('name',)


admin.site.register(Realtor,RealtorsAdmin)
