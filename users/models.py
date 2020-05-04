from django.db import models
AUTH_USER_MODEL='users.CustomUser'
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

#class Siteuser(models.Model):
   # First_name=models.CharField(max_length=100)
  #  Last_name=models.CharField(max_length=100)
  #  Password1=models.CharField(max_length=100)
  #  Password2=models.CharField(max_length=100)

