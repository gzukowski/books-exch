# admin.py
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Book
from .tasks import fetch_top_books

class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [ path('api-upload/', self.upload, name="upload") ]
        return new_urls + urls
        
    def upload(self, request):
        fetch_top_books.delay(request.user.id)
        self.message_user(request, "Data imported successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))

admin.site.register(Book, BookAdmin)
