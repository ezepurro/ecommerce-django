# Generated by Django 5.0.1 on 2024-07-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='store', verbose_name='Image'),
        ),
    ]
