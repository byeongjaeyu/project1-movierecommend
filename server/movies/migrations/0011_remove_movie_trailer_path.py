# Generated by Django 3.2.3 on 2021-11-23 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_movie_trailer_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='trailer_path',
        ),
    ]
