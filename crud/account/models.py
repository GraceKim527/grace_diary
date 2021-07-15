from django.db import models

# Create your models here.
class UserInformation(models.Model):
    age = models.CharField(max_length=20)
    address = models.CharField(max_length=200)