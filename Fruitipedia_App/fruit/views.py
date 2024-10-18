from django.shortcuts import render, redirect
from Fruitipedia_App.fruit.forms import FruitForm, FruitEditForm, DeleteFruitForm
from Fruitipedia_App.fruit.models import Fruit
from Fruitipedia_App.user.models import Profile


def create_fruit(request):
    profile = Profile.objects.first()
    form = FruitForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.owner = profile
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    profile = Profile.objects.first()
    fruit = profile.fruits.get(pk=pk)
    context = {
        'profile': profile,
        'fruit': fruit
    }
    return render(request, 'fruit/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = FruitEditForm(instance=fruit)

    if request.method == 'POST':
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruit/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    form = DeleteFruitForm(instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruit/delete-fruit.html', context)




















