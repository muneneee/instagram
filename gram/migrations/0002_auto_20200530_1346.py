# Generated by Django 2.2 on 2020-05-30 10:46

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]