# Generated by Django 2.2 on 2020-12-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20201224_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='daily_intakes_max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='daily_intakes_min',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='item_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='item_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='meal_relation',
            field=models.CharField(blank=True, choices=[('B', 'Before meal'), ('W', 'With meal'), ('A', 'After meal')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='neurotransmitters',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.Neurotransmitter'),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='portion_weight_max',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='portion_weight_min',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='catalog.Tag'),
        ),
    ]
