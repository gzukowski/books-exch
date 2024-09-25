from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Exchange, Book
from ..forms import ExchangeForm

def request_exchange(request, book_id):
    if not request.user.is_authenticated:
        messages.warning(request, "You need to log in to request an exchange.")
        return redirect('home')

    receiver_book = Book.objects.get(id=book_id)
    
    if receiver_book.owner == request.user:
        messages.error(request, "You cannot offer a trade for your own book.")
        return redirect('profile') 
    
    receiver = receiver_book.owner

    if request.method == 'POST':
        form = ExchangeForm(request.POST, user=request.user)
        if form.is_valid():
            exchange = form.save(commit=False)
            exchange.requester = request.user
            exchange.receiver = receiver
            exchange.receiver_book = receiver_book
            exchange.save()
            messages.success(request, 'Exchange request sent!')
            return redirect('profile')
    else:
        form = ExchangeForm(user=request.user)

    return render(request, 'request_exchange.html', {'form': form, 'receiver_book': receiver_book})

def respond_exchange(request, exchange_id, response):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to respond to an exchange.')
        return redirect('home')

    exchange = get_object_or_404(Exchange, id=exchange_id, receiver=request.user)

    if response == 'accept':
        exchange.status = 'accepted'
        messages.success(request, 'Exchange accepted!')
    elif response == 'decline':
        exchange.status = 'declined'
        messages.warning(request, 'Exchange declined.')

    exchange.response_date = timezone.now()
    exchange.save()

    return redirect('profile')
    
