from django.shortcuts import render, get_object_or_404
from  django.views import generic, View
from .models import Recipe

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class DinnerList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=0).order_by('-created_on')
    
    template_name = 'dinner.html'
    paginate_by = 6


class CoctailesList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=2).order_by('-created_on')
    
    template_name = 'coctailes.html'
    paginate_by = 6

class SweetsList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, category=1).order_by('-created_on')
    
    template_name = 'sweets.html'
    paginate_by = 6

