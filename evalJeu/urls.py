"""evalJeu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


import authentification.views
import eval.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.login_page, name='login'),
    path('logout', authentification.views.logout_user, name='logout'),
    path('signup', authentification.views.signup_page, name='signup'),

    path('account', eval.views.account_page, name='my-account'),
    path('account-informations', eval.views.display_informations, name='informations'),
    path('update-infrmations', eval.views.update_informations, name='update'),
    path('delete-account', eval.views.delete_account, name='delete'),
    path('chage-password', eval.views.change_password, name='change_password'),

    path('home/', eval.views.home, name='home'),
    path('display-games/', eval.views.display_games, name="display-games"),
    path('display-game/<int:id>', eval.views.display_informations_game, name='informations'),
    path('write-review', eval.views.write_review, name='write_review'),
    path('add-coins/', eval.views.add_coins, name='add-coins'),
    path('promote/', eval.views.promote, name='promote'),
    path('change-role/<int:user_id>/', eval.views.change_user_role, name='change-user-role'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
