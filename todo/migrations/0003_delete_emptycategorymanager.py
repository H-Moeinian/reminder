# Generated by Django 3.2.5 on 2021-07-28 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_emptycategorymanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmptyCategoryManager',
        ),
    ]
