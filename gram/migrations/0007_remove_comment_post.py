# Generated by Django 2.2 on 2020-05-31 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0006_auto_20200531_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
