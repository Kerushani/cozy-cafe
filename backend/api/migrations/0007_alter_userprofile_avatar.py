# Generated by Django 4.2.20 on 2025-05-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_watchlistitem_imdb_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(default='https://api.dicebear.com/7.x/initials/svg'),
        ),
    ]
