from django.shortcuts import render
from utils.recipes.factory import request_recipes

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [request_recipes() for _ in range(9)],
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': request_recipes(),
        'is_detail_page': True,
    })