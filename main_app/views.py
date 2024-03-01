from django.shortcuts import render, redirect

# Add the following import
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Console
from .forms import TypeForm

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
def home(request):
  return render(request, 'home.html')

# def about(request):
#   return HttpResponse('<h1>About Gamer</h1>')

def about(request):
  return render(request, 'about.html')

def game_index(request):
  games=Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def game_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  # return render(request, 'games/detail.html', { 'game': game })
  no_consoles = Console.objects.exclude(id__in = game.consoles.all().values_list('id'))
  type_form = TypeForm()
  return render(request, 'games/detail.html', {
    'game': game, 'type_form': type_form, 'consoles': no_consoles
  })

def console_list(request, game_id, console_id):
  Game.objects.get(id=game_id).consoles.add(console_id)
  return redirect('game-detail', game_id=game_id)

def add_type(request, game_id):
  # create a ModelForm instance using the data in request.POST
  form = TypeForm(request.POST)
  # validate the form
  if form.is_valid():
    
    new_type = form.save(commit=False)
    new_type.game_id = game_id
    new_type.save()
  return redirect('game-detail', game_id=game_id)

class GameCreate(CreateView):
  model = Game
  # fields = '__all__'
  fields = ['name', 'description', 'release_year']
  success_url = '/games/'

class GameUpdate(UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

class ConsoleCreate(CreateView):
  model = Console
  fields = '__all__'
  success_url = '/consoles/'

class ConsoleList(ListView):
  model = Console

class ConsoleDetail(DetailView):
  model = Console 

class ConsoleUpdate(UpdateView):
  model = Console
  fields = '__all__'

class ConsoleDelete(DeleteView):
  model = Console
  success_url = '/consoles/'