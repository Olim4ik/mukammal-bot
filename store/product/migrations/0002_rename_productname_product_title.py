# Generated by Django 5.0.2 on 2024-02-08 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='title',
        ),
    ]
