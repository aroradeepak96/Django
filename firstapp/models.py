from django.db import models

# Create your models here.
from django.db import models

class Candidate(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Email_Id= models.CharField(max_length=30)
    
class python(models.Model):
    session=models.CharField(max_length=30,unique=True)
    
    def __str__(self):
        return self.session

class student(models.Model):
    name=models.CharField(max_length=30,unique=False)
    session=models.ForeignKey("Python",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Login(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.username


