import requests
from celery import shared_task
from .models import Book
from django.contrib.auth.models import User

@shared_task
def fetch_top_books(user_id):
    url = "https://www.googleapis.com/books/v1/volumes?q=top&maxResults=40"
    response = requests.get(url)
    user = User.objects.get(id=user_id)
    
    if response.status_code == 200:
        books_data = response.json().get("items", [])
        for item in books_data:
            volume_info = item.get("volumeInfo", {})
            title = volume_info.get("title")
            authors = ', '.join(volume_info.get("authors", []))
            description = volume_info.get("description", '')
            condition = 'New'
            image_url = volume_info.get("imageLinks", {}).get("thumbnail")
            
            if title and len(title) > 255:
                title = title[:255]
            if authors and len(authors) > 255:
                authors = authors[:255]
            if description and len(description) > 1000:
                description = description[:1000]
            if condition and len(condition) > 50:
                condition = condition[:50]
                

            if not Book.objects.filter(title=title).exists():
                book = Book(
                    title=title,
                    author=authors,
                    description=description,
                    condition=condition,
                    image=None,
                    external_image=image_url,
                    owner = user
                )
                book.save()
    else:
        print("Error:", response.status_code)
