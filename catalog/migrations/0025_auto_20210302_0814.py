# Generated by Django 3.1.6 on 2021-03-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0024_auto_20210215_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producent',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['name']},
        ),
    ]
