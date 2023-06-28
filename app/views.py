from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import Recipe
from .forms import RecipeForm

# Create your views here.


def home(request):
    recipes = Recipe.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        recipes = Recipe.objects.filter(recipe_name__icontains=search)
    context = {'recipes': recipes}
    return render(request, 'index.html', context)


@login_required(login_url='/login/ ')
def create_recipe(request):
    recipe_form = RecipeForm()

    if request.method == 'POST':
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')

        obj = Recipe.objects.create(
            recipe_name=name,
            recipe_description=description,
            recipe_image=image)
        return redirect('home')

    context = {'form': recipe_form}
    return render(request, 'app/recipe_form.html', context)


def delete_recipe(request, id):
    obj = Recipe.objects.get(id=id)
    obj.delete()
    return redirect('home')


def update_recipe(request, id):
    obj = Recipe.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')

        obj.recipe_name = name
        obj.recipe_description = description
        if image:
            obj.recipe_image = image
        obj.save()
        return redirect('home')
    context = {'recipe': obj}
    return render(request, 'app/update.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exists")
            return redirect('login')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Id and password")
        else:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'app/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username Already Taken")
            return redirect('register')

        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        messages.info(request, "Registration Successfull")
        return redirect('register')

    context = {}
    return render(request, 'app/register.html', context)
