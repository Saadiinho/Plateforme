# Generated by Django 3.2.20 on 2023-07-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0005_alter_user_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='review_number',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
