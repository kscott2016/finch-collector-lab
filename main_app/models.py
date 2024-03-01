from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPES = (
  ('A', 'Adventure'),
  ('F', 'Fantasy'),
  ('R', 'RPG'),
  ('B', 'Fighting'),
  ('S', 'Shooter'),
  ('O', 'Other'),
)

class Console(models.Model):
  name = models.CharField(max_length=50)
  company = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('console-detail', kwargs={'pk': self.id})

class Game(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release_year = models.IntegerField()
  consoles = models.ManyToManyField(Console)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('cat-detail', kwargs={'cat_id': self.id})
  
  def is_interesting_game(self):
    
    if self.type_set.count()==0 or self.type_set.count()<3:
      return False
    elif self.type_set.count()>=3:
      return True

    # return self.type_set.filter(self.type).count() >= 3
  
class Type(models.Model):
  type = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TYPES,
    # set the default value for meal to be 'B'
    default=TYPES[0][0])
  max_players=models.IntegerField('Max number of players')

  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    
    return f"{self.get_type_display()}"
