from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from eval.models import Game, Review
from authentification.models import User
from django.core.paginator import Paginator
from eval.forms import ReviewForm, AddCoinsForm, ChangeRoleFrom




@login_required
def home(request):
    return render(request, 'eval/home.html')

@login_required
def account_page(request):
    return render(request, 'eval/account.html')

@login_required
def display_informations(request):
    return render(request, 'eval/informations.html')

@login_required
def update_informations(request):
    User = get_user_model()
    user = request.user
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        email = request.POST.get('email')
        if pseudo:
            if User.objects.filter(username=pseudo).exists():
                # Le pseudo est déjà pris
                return render(request, 'eval/update_informations.html', {'error': 'Ce pseudo est déjà utilisé.'})
            else:
                user.username = pseudo
        if firstName :
            user.first_name = firstName
        if lastName :
            user.last_name = lastName
        if email : 
            user.email = email
        user.save()
        return redirect('informations')
    return render(request, 'eval/update_informations.html')

@login_required
def delete_account(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        logout(request)
        return redirect('login')
    return render(request, 'eval/delete_account.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mettre à jour la session de l'utilisateur pour éviter une déconnexion
            return redirect('my-account')  # Redirigez l'utilisateur vers la page de profil ou une autre page après la modification du mot de passe
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'eval/change_password.html', {'form': form})


@login_required
def display_games(request):
    games = Game.objects.all()
    #Partie de filtrage
    if request.method == 'POST':
        # Filtrage par jetons
        filter_coins = request.POST.get('coins')
        if filter_coins == '1':
            coins = Game.objects.all().order_by('coins')
        elif filter_coins == '2':
            coins = Game.objects.all().order_by('-coins')
        else:
            coins = games
        #Filtrage par date de sortie
        filter_date = request.POST.get('date')
        if filter_date == '1':
            date = Game.objects.all().order_by('year_of_Release')
        elif filter_date == '2':
            date = Game.objects.all().order_by('-year_of_Release')
        else : 
            date = games
        games = coins & date
    item_name = request.GET.get('search')
    if item_name != '' and item_name is not None:
        games = Game.objects.filter(name__icontains=item_name)
    paginator = Paginator(games, 12)
    page = request.GET.get('page')
    games = paginator.get_page(page)
    return render(request, 'eval/display_games.html', {'games': games})

def display_informations_game(request, id):
    user = request.user
    game = Game.objects.get(id=id)
    reviews = Review.objects.all()
    score = 0
    count = 0
    confirmation = False
    for review in reviews :
        if review.game.name == game.name:
            score = score + review.score
            count = count + 1
    if count != 0:
        score = score / count
    if request.method == 'POST':
        confirmation = True
    return render(request, 'eval/display_informations_game.html', {'game': game, 'reviews': reviews, 'score': score, 'count': count, 'user': user, 'confirmation': confirmation})

@login_required
def write_review(request):
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.save()
            user.coins += 1
            user.review_number += 1
            user.save()
            return redirect('display-games')
    else :    
        form = ReviewForm()
    return render(request, 'eval/write_review.html', {'form': form})

@login_required
def add_coins(request):
    user = request.user
    error = False
    if request.method == 'POST':
        form = AddCoinsForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            game_value = form.cleaned_data['game']
            if number > user.coins:
                error = True
            else :
                game = game_value
                game.coins += number
                user.coins = user.coins - number
                user.save()
                game.save()
                return redirect('display-games')
    else :
        form = AddCoinsForm()
    return render(request, 'eval/add_coins.html', {'form': form, 'error': error})

@login_required
def promote(request):
    users = User.objects.all()
    return render(request, 'eval/promote.html', {'users': users})

@login_required
def change_user_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = ChangeRoleFrom(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('promote')  # Rediriger vers la liste des utilisateurs ou une autre page
    else:
        form = ChangeRoleFrom(instance=user)

    return render(request, 'eval/change_user_role.html', {'form': form, 'user': user})
    
    

