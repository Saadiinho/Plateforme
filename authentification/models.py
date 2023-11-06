from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ADMINISTRATOR = 'ADMINISTRATOR'
    TESTEUR = 'TESTEUR'
    PLAYER = 'PLAYER'

    ROLE_CHOICES = (
        (ADMINISTRATOR, 'ADMINISTRATOR'),
        (TESTEUR, 'TESTEUR'),
        (PLAYER, 'PLAYER'),
    )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='rôle', default=PLAYER)
    coins = models.PositiveBigIntegerField(default=3)
    review_number = models.PositiveBigIntegerField(default=0)
