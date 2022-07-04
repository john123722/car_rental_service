# Generated by Django 4.0.4 on 2022-07-04 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentapp', '0010_reviews_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='c_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='car_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentapp.car', verbose_name='car_name'),
        ),
    ]