from django.contrib import admin
from .models import Game, Type, Console

# Register your models here.
admin.site.register(Game)
admin.site.register(Type)
admin.site.register(Console)