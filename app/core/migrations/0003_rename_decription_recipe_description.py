# Generated by Django 3.2.25 on 2024-04-14 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='decription',
            new_name='description',
        ),
    ]