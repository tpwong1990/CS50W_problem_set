# Generated by Django 4.1.7 on 2023-02-25 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_list_watch_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='no_bid',
        ),
        migrations.AddField(
            model_name='list',
            name='no_bid',
            field=models.IntegerField(default=0),
        ),
    ]