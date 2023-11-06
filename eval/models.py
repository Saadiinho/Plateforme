from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from authentification.models import User


class Game(models.Model):
    name = models.CharField(max_length=500)
    platform = models.CharField(max_length=100)
    year_of_Release = models.IntegerField()
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='')
    coins = models.PositiveBigIntegerField()
    def __str__(self):
        return f'{self.name}'

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.game}'