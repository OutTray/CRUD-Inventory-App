# Generated by Django 4.0.1 on 2022-01-14 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory_db',
            name='item_id',
        ),
    ]
