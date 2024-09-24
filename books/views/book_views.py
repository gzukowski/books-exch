from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Book
from ..forms import BookForm

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def browser(request):
    return render(request, 'browser.html', {})

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    
    results = []
    for book in books:
        if book.image:
            image = book.image_file.url
        elif book.external_image:
            image = book.external_image
        else:
            image = '/static/default_book_image.jpg'
        
        results.append({
            'id': book.id,
            'title': book.title,
            'image': image
        })
    
    return JsonResponse({'books': results})

def book_page(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book.html', {'book': book})

def add_book(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('profile')

    return render(request, 'add_book.html', {'form': form})

def remove_book(request, book_id):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, id=book_id)
        
        if book.owner == request.user:
            book.delete()
            return redirect('profile')
        
        return redirect('home') 
    else:
        return redirect('home')
