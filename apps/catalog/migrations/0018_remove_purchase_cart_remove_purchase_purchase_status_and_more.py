# Generated by Django 5.0.4 on 2024-06-07 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_purchase_delete_purchases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='purchase_status',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.DeleteModel(
            name='Purchase_status',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
