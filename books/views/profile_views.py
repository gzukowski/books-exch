
from django.shortcuts import render, redirect
from ..models import Book

def profile(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
        return render(request, 'profile.html', {'books': books})
    else:
        return redirect('home')
