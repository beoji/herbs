# Generated by Django 3.1.6 on 2021-02-15 15:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0023_supplement_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
