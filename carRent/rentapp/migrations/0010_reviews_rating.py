# Generated by Django 4.0.4 on 2022-06-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0009_rename_usernames_reviews_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]