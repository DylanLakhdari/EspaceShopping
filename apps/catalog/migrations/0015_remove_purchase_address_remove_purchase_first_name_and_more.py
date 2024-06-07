# Generated by Django 5.0.4 on 2024-06-07 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_remove_purchase_cart_remove_purchase_purchase_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='address',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='orders',
        ),
        migrations.AddField(
            model_name='purchase',
            name='cart',
            field=models.ManyToManyField(to='catalog.cart'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchase_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.purchase_status'),
        ),
    ]
