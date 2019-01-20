from django.db import models

# Create your models here.
class CustomModel(models.Model):
    firstName=models.CharField(max_length=120)
    lastName=models.CharField(max_length=120)
    username=models.CharField(max_length=150)
    email=models.EmailField(blank=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
