# Generated by Django 3.0.7 on 2020-06-07 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='projects',
            new_name='project',
        ),
    ]