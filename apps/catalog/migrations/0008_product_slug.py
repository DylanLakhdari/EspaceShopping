# Generated by Django 5.0.4 on 2024-04-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_product_discount_product_thumbnail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
