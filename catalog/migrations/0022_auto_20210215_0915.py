# Generated by Django 3.1.6 on 2021-02-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20210215_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='item_weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='portion_weight_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='portion_weight_min',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True),
        ),
    ]
