# Generated by Django 4.0.4 on 2022-06-27 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0008_alter_reviews_car_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='usernames',
            new_name='username',
        ),
    ]
