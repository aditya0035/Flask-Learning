from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class UserPortFolioInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    profilePhoto=models.ImageField(upload_to="profiepic/%y%m%d",blank=True)
    About=models.TextField(blank=True)
