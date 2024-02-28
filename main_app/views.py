from django.shortcuts import render

# Add the following import
# from django.http import HttpResponse

class Game:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, release_year):
    self.name = name
    self.description = description
    self.release_year = release_year

games = [

  Game('Kingdom Hearts', 'disney fighters and exploring', 2002),
  Game('Crash Bandicoot: Warped', 'mutated bandicoot defeats scientist', 1998)
]

# Define the home view
# def home(request):
#   return HttpResponse('<h1>Hello Gamer</h1>')
def home(request):
  return render(request, 'home.html')

# def about(request):
#   return HttpResponse('<h1>About Gamer</h1>')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  return render(request, 'games/index.html', { 'games': games })