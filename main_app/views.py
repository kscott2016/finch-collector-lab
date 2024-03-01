from django.shortcuts import render, redirect

# Add the following import
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game, Console
from .forms import TypeForm

from django.contrib.auth.views import LoginView

# class Game:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, description, release_year):
#     self.name = name
#     self.description = description
#     self.release_year = release_year

# games = [

#   Game('Kingdom Hearts', 'disney fighters and exploring', 2002),
#   Game('Crash Bandicoot: Warped', 'mutated bandicoot defeats scientist', 1998)
# ]

# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello Gamer</h1>')

# def home(request):
#   return render(request, 'home.html')
class Home(LoginView):
  template_name = 'home.html'

# def about(request):
#   return HttpResponse('<h1>About Gamer</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def game_index(request):
  # games=Game.objects.all()
  games=Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 'games': games })

@login_required
def game_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  # return render(request, 'games/detail.html', { 'game': game })
  no_consoles = Console.objects.exclude(id__in = game.consoles.all().values_list('id'))
  type_form = TypeForm()
  return render(request, 'games/detail.html', {
    'game': game, 'type_form': type_form, 'consoles': no_consoles
  })

@login_required
def console_list(request, game_id, console_id):
  Game.objects.get(id=game_id).consoles.add(console_id)
  return redirect('game-detail', game_id=game_id)

@login_required
def add_type(request, game_id):
  # create a ModelForm instance using the data in request.POST
  form = TypeForm(request.POST)
  # validate the form
  if form.is_valid():
    
    new_type = form.save(commit=False)
    new_type.game_id = game_id
    new_type.save()
  return redirect('game-detail', game_id=game_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('game-index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  # fields = '__all__'
  fields = ['name', 'description', 'release_year']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  success_url = '/games/'

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['name', 'description', 'release_year']

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  fields = ['name', 'description', 'release_year']
  success_url = '/games/'

class ConsoleCreate(LoginRequiredMixin, CreateView):
  model = Console
  fields = '__all__'
  success_url = '/consoles/'

class ConsoleList(LoginRequiredMixin, ListView):
  model = Console

class ConsoleDetail(LoginRequiredMixin, DetailView):
  model = Console 

class ConsoleUpdate(LoginRequiredMixin, UpdateView):
  model = Console
  fields = '__all__'

class ConsoleDelete(LoginRequiredMixin, DeleteView):
  model = Console
  success_url = '/consoles/'