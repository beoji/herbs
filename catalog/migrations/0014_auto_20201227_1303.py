# Generated by Django 2.2 on 2020-12-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_supplement_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='item_weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
    ]
