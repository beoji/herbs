# Generated by Django 3.1.6 on 2021-02-15 14:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0022_auto_20210215_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplement',
            name='users',
            field=models.ManyToManyField(related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
