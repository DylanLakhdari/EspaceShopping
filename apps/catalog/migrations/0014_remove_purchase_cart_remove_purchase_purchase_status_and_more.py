# Generated by Django 5.0.4 on 2024-06-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_remove_purchase_adress'),
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
        migrations.AddField(
            model_name='purchase',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='purchase',
            name='first_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='purchase',
            name='last_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='purchase',
            name='orders',
            field=models.ManyToManyField(to='catalog.order'),
        ),
    ]
