# Generated by Django 4.2.2 on 2023-06-11 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_name_product_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='p_name',
        ),
    ]