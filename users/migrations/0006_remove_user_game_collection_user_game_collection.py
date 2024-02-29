# Generated by Django 5.0.2 on 2024-02-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_game_collection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='game_collection',
        ),
        migrations.AddField(
            model_name='user',
            name='game_collection',
            field=models.JSONField(blank=True, default=list),
        ),
    ]