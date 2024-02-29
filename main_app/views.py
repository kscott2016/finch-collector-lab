from django.shortcuts import render, redirect

# Add the following import
# from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
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
  type_form = TypeForm()
  return render(request, 'games/detail.html', {
    'game': game, 'type_form': type_form
  })

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
  fields = '__all__'
  success_url = '/games/'

class GameUpdate(UpdateView):
  model = Game
  fields = '__all__'

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'