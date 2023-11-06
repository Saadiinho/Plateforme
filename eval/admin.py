from django.contrib import admin
from eval.models import Game
from eval.models import Review
from authentification.models import User

admin.site.register(Game)
admin.site.register(Review)
admin.site.register(User)
# Register your models here.
