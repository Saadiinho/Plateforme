# Generated by Django 3.2.20 on 2023-07-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eval', '0003_game_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
