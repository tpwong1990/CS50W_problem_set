# Generated by Django 4.1.7 on 2023-04-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopping', '0007_user_phone_no_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]