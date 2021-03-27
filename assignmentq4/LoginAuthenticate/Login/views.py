from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {'form': form})

def home(request):
    return render(request, "home.html")
