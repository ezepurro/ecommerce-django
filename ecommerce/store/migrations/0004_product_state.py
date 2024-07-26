# Generated by Django 5.0.1 on 2024-07-26 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.CharField(choices=[('New', 'New'), ('Used as new', 'Used as new'), ('Used', 'Used'), ('Refurbished', 'Refurbished')], default='Used', max_length=20),
        ),
    ]
