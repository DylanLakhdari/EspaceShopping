# Generated by Django 5.0.4 on 2024-06-07 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_purchase_status_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='adress',
        ),
    ]
