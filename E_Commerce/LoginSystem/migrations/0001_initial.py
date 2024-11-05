# Generated by Django 4.1 on 2024-11-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('Immigration_Status', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
