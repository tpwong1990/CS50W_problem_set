# Generated by Django 4.1.7 on 2023-03-08 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
    ]
