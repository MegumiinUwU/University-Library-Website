from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile3'),
    path('home/', views.home, name='home3'),
    path('search/', views.search, name='search3'),
    path('logout/', views.logout_view, name='logout3'),
    path('addpage/', views.addpage, name='addpage3'),
    path('addbook/', views.addbook, name='addbook3'),
    path('get-all-books/', views.admin_book_list, name='get_all_books3'),
    path('get-book-details/', views.get_book_details, name='get_book_details'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('get-random-books/', views.get_random_books, name='get_random_books2'),
    path('get-random-quote/', views.get_random_quote, name='get_random_quote2'),

]