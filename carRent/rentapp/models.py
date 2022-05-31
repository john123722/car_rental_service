from datetime import date
from django.db import models

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

