from django.shortcuts import render, redirect

from Fruitipedia_App.user.forms import UserForm, EditUserForm, DeleteUserForm
from Fruitipedia_App.user.models import Profile


def create_profile(request):
    form = UserForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'user/create-profile.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    fruits_all = profile.fruits.count()

    context = {
        'profile': profile,
        'fruits_all': fruits_all
    }

    return render(request, 'user/details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    form = EditUserForm(instance=profile)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details-profile')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'user/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    form = DeleteUserForm(request.POST)

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, 'user/delete-profile.html', context)














