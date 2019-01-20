from django.db import models

# Create your models here.
class UserData(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"