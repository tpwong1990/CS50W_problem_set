# Generated by Django 4.1.7 on 2023-04-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopping', '0017_item_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.CharField(max_length=20),
        ),
    ]
