# Generated by Django 3.1.2 on 2020-10-19 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squirrelapp', '0002_auto_20201018_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirreldetails',
            name='Longitude',
        ),
    ]
