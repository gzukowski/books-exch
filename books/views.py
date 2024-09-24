from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books' : books})

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

def browser(request):
    return render(request, 'browser.html', {})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    results = [{'id': book.id, 'title': book.title, 'image': book.image.url} for book in books]
    return JsonResponse({'books': results})

def book_page(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    return render(
        request,
        'book.html',
        {'book': book}
    )
    
def profile(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
        return render(request, 'profile.html', {'books': books})
    else:
        return redirect('home')

def remove_book(request, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        
        if book.owner == request.user:
            book.delete()
            return redirect('profile')
        
        return redirect('home') 
    else:
        return redirect('home')
    
def add_book(request):
    form = BookForm()
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return redirect('login')
        
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('profile')
        
    return render(request, 'add_book.html', {'form': form})
    
    
    