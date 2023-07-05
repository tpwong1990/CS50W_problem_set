# Generated by Django 4.1.7 on 2023-02-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_bid_price_list_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default=models.DecimalField(decimal_places=2, max_digits=20), max_digits=20),
        ),
    ]