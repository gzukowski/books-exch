from django.contrib import admin
from django.urls import path, include
from .views.auth_views import login_user, logout_user, register_user
from .views.book_views import home, search_books, book_page, add_book, remove_book, browser
from .views.profile_views import profile
from .views.exchange_views import request_exchange, respond_exchange

urlpatterns = [
    path('', home, name="home"),
    path('register/', register_user, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('browser/', browser, name='browser'),
    path('search/', search_books, name='search_books'),
    path('books/<int:book_id>/', book_page, name='book_page'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/remove/', remove_book, name='remove_book'),
    path('profile/', profile, name='profile'),
    path('exchange/request/<int:book_id>/', request_exchange, name='request_exchange'),
    path('exchange/respond/<int:exchange_id>/<str:response>/', respond_exchange, name='respond_exchange'),
]