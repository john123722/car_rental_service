# Generated by Django 4.0.4 on 2022-05-30 15:36

from dataclasses import field, fields
from django.db import migrations, models
from django.contrib.auth.models import User
from rentapp.models import car


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('email', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=15)),
                ('reason', models.TextField()),
                ('date', models.DateField()),
            ], 
           ),
        migrations.CreateModel(
            name='car',
            fields= [
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length= 300)),
                ('quantity', models.IntegerField)

            ],
           ),
        migrations.CreateModel(
             name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.ForeignKey(User, verbose_name="username", on_delete=models.CASCADE)),
                ('rating', models.IntegerField()),
                ('cars', models.ForeignKey(car,verbose_name="cars",on_delete=models.CASCADE))    
            ],
           ),
    ]
