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
    price = models.IntegerField(default)
    description = models.TextField(max_length= 300)
    quantity = models.IntegerField(default)
    id = models.IntegerField(primary_key=TRUE)

class review(models.Model):
    username = models.ForeignKey(User, verbose_name="username", on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=TRUE)
    rating = models.IntegerField()
    cars = models.ForeignKey(car,verbose_name="cars",on_delete=models.CASCADE)

