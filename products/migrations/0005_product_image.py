# Generated by Django 5.2 on 2025-05-23 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
