from django.contrib import admin
from rentapp.models import Contact
from rentapp.models import login
from rentapp.models import car
from rentapp.models import reviews
# Register your models here.
admin.site.register(Contact)
admin.site.register(login)
admin.site.register(car)
admin.site.register(reviews)