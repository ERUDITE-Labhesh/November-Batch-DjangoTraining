# Generated by Django 4.1 on 2024-11-05 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LoginSystem', '0004_rename_password_loginsystem_passwords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginsystem',
            old_name='passwords',
            new_name='password',
        ),
    ]
