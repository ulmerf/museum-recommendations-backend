# Generated by Django 3.2.4 on 2021-06-26 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_objects', '0002_rename_museum_id_museumobject_inventory_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='museumobject',
            old_name='name',
            new_name='title',
        ),
    ]