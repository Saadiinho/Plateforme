from django import forms
from eval.models import Review
from eval.models import Game
from authentification.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude =['user']

class AddCoinsForm(forms.Form):
    number = forms.IntegerField(label='Nombre', min_value=0)
    game = forms.ModelChoiceField(queryset=Game.objects.all(), label='Jeu')

class ChangeRoleFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['role']