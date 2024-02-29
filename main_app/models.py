from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Game(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release_year = models.IntegerField()
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('cat-detail', kwargs={'cat_id': self.id})