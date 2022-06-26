# Generated by Django 4.0.4 on 2022-06-22 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0003_review_alter_car_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
        migrations.AddField(
            model_name='review',
            name='car',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='rentapp.car', verbose_name='car'),
            preserve_default=False,
        ),
    ]