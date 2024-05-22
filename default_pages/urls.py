from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('view_books/', views.view_books, name='view_books'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('get-random-books/', views.get_random_books, name='get_random_books'),
    path('get-random-quote/', views.get_random_quote, name='get_random_quote'),
    path('get-book-details/', views.get_book_details, name='get_book_details'),
]
