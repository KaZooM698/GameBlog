from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm


from .models import Games, Category
from .forms import GamesForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,  'Регистрация прошла успешно')
            return redirect('Login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'Games/register.html', {'form': form})

def login(request):
    return render(request, 'Games/login.html')

class HomeGames(ListView):
    model = Games
    context_object_name = 'games'
    template_name = 'Games/home_games_list.html'
    extra_context = {'title': 'Главная'}
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Главная страница'
        return context

    def get_queryset(self):
        return Games.objects.filter(is_published=True).select_related('category')
#
class GamesByCategory(ListView):
    model = Games
    template_name = 'Games/home_games_list.html'
    context_object_name = 'games'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Games.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

class AddGames(CreateView):
    form_class = GamesForm
    template_name = 'Games/add_games.html'

# class ViewGames(DetailView):
#     model = Games
#     context_object_name = 'games_item'
#     template_name = 'Games/home_games_list.html'
#     extra_context = {'title': 'Главная'}
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title']= 'Главная страница'
#         return context
#
#     def get_queryset(self):
#         return Games.objects.filter(is_published=True)

# def index(request):
#     games = Games.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'games': games,
#         'title': 'Список игр',
#         #'categories': categories
#     }
#     return render(request, 'Games/index.html', context=context)

# def get_category(request, category_id):
#     games = Games.objects.filter(category_id = category_id)
#     categories = Category.objects.all()
#     category=Category.objects.get(pk=category_id)
#     context = {
#         'games': games,
#         'category': category,
#         #'categories': categories
#     }
#     return render(request, 'Games/category.html', context=context)

def view_games(request, games_id):
    #games_item = Games.objects.get(pk=games_id)
    games_item = get_object_or_404(Games, pk=games_id)
    context = {
        'games_item': games_item
    }
    return render(request, 'games/view_games.html', context=context)

# def add_games(request):
#     if request.method == 'POST':
#         form = GamesForm(request.POST)
#         if form.is_valid():
#             #games = Games.objects.create(**form.cleaned_data)
#             games = form.save()
#             return redirect(games)
#     else:
#         form = GamesForm()
#     return render(request, 'Games/add_games.html', {'form': form})