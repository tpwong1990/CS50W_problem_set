# Generated by Django 4.1.7 on 2023-03-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_no',
            field=models.PositiveIntegerField(),
        ),
    ]
