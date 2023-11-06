# Generated by Django 3.2.20 on 2023-07-26 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eval', '0006_game_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to='authentification.user'),
            preserve_default=False,
        ),
    ]