from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

TYPES = (
  ('A', 'Adventure'),
  ('F', 'Fantasy'),
  ('R', 'RPG'),
  ('B', 'Fighting'),
  ('S', 'Shooter'),
)

class Game(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release_year = models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('cat-detail', kwargs={'cat_id': self.id})
  
class Type(models.Model):
  type = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=TYPES,
    # set the default value for meal to be 'B'
    default=TYPES[0][0])
  max_players=models.IntegerField()

  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    
    return f"{self.get_types_display()}. Allows {self.max_players} to play"