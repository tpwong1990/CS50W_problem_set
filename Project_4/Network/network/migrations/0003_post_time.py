# Generated by Django 4.1.7 on 2023-03-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_remove_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
