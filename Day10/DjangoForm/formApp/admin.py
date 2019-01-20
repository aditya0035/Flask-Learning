from django.contrib import admin
from . import models
# Register your models here.
class UserDataAdminModel(admin.ModelAdmin):
    list_display=('firstName', 'lastName')
    list_display_link=('id',)
    
admin.site.register(models.UserData,UserDataAdminModel)