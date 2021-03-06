# Generated by Django 2.2 on 2020-12-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20201227_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplement',
            name='neurotransmitters',
            field=models.ManyToManyField(blank=True, to='catalog.Neurotransmitter'),
        ),
        migrations.AlterField(
            model_name='supplement',
            name='tags',
            field=models.ManyToManyField(blank=True, to='catalog.Tag'),
        ),
    ]
