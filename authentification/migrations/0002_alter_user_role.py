# Generated by Django 3.2.20 on 2023-07-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMINISTRATOR', 'ADMINISTRATOR'), ('TESTEUR', 'TESTEUR'), ('PLAYER', 'PLAYER')], max_length=30, verbose_name='rôle'),
        ),
    ]
