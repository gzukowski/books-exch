from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'home.html', {})

def register_user(request):
    return render(request, 'register.html', {})

def login_user(request):
    return render(request, 'login.html', {})

def logout_user(request):
    return render(request, 'logout.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an erorr")
            return redirect('login')
            
    else: 
        return render(
            request,
            'login.html',
            {}
        )
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered and logged in")
            return redirect('home')
        
        else:
            messages.error(request, "Failed to register. Please correct the errors below.")
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})