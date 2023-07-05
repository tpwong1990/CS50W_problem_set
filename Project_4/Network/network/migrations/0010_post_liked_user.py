# Generated by Django 4.1.7 on 2023-03-27 10:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_alter_like_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_user',
            field=models.ManyToManyField(related_name='liked_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
