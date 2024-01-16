from django.contrib import admin
from django.urls import path

from Games.views import HomeGames, GamesByCategory, view_games, AddGames, register, login
#from Games.views import index, get_category, ViewGames, add_games
urlpatterns = [
    # path('', index, name='Home'),
    # path('category/<int:category_id>', get_category, name='Category'),
    # path('games/<int:pk>', GamesByCategory.as_view(), name='View_games'),
    # path('games/add_games', add_games, name='Add_games')
    path('games/<int:games_id>', view_games, name='View_games'),
    path('', HomeGames.as_view(), name='Home'),
    path('category/<int:category_id>', GamesByCategory.as_view(), name='Category'),
    path('games/add_games', AddGames.as_view(), name='Add_games'),
    path('register', register, name='Register'),
    path('login', login, name='Login')

]

