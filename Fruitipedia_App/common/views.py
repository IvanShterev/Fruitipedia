from django.shortcuts import render
from Fruitipedia_App.fruit.models import Fruit
from Fruitipedia_App.user.models import Profile


def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }

    return render(request, 'index.html', context)


def dashboard(request):
    profile = Profile.objects.first()
    fruits = profile.fruits.all()

    context = {
        'profile': profile,
        'fruits': fruits
    }

    return render(request, 'dashboard.html', context)