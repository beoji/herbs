# Generated by Django 2.2 on 2020-12-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20201225_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
