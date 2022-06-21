from datetime import date
from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length= 75)
    email = models.CharField(max_length= 150)
    contact =  models.CharField(max_length= 15)
    reason = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class login(models.Model):
    username = models.CharField(max_length= 75)
    password = models.CharField(max_length= 75)

class car(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length= 300)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='static/uploads')

class review(models.Model):
    name = models.CharField(max_length=50)
    rating = models.IntegerField(default= 0)
    description = models.CharField(max_length=300)





