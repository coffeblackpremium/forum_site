# Generated by Django 3.2.8 on 2021-10-19 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='name',
            new_name='nome',
        ),
    ]
