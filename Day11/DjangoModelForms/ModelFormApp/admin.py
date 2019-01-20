from django.contrib import admin
from . import models
# Register your models here.
class CustomModelAdminModel(admin.ModelAdmin):
    list_display=('id','username')
    

admin.site.register(models.CustomModel,CustomModelAdminModel)