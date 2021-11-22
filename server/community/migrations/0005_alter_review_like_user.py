# Generated by Django 3.2.3 on 2021-11-19 04:02
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_review_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_user',
            field=models.ManyToManyField(blank=True, related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
