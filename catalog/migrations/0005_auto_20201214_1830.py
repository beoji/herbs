# Generated by Django 2.2 on 2020-12-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201214_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='bioavailability',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]