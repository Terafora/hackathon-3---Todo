# Generated by Django 4.2.7 on 2023-11-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
