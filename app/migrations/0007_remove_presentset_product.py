# Generated by Django 3.0.7 on 2020-10-21 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20201021_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentset',
            name='product',
        ),
    ]
