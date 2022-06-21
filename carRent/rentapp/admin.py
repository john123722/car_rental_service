from django.contrib import admin
from rentapp.models import Contact, car
from rentapp.models import login
# Register your models here.
admin.site.register(Contact)
admin.site.register(login)
admin.site.register(car)