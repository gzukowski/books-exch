
from django.shortcuts import render, redirect
from ..models import Book, Exchange

def profile(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
        exchanges_received = Exchange.objects.filter(receiver=request.user, status='pending')
        exchanges_requested = Exchange.objects.filter(requester=request.user)
        return render(
            request,
            'profile.html',
            {
                'books': books,
                'exchanges_received': exchanges_received,
                'exchanges_requested': exchanges_requested,
            })
    else:
        return redirect('home')
