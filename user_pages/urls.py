from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile2'),
    path('home/', views.home, name='home2'),
    path('inventory/', views.inventory, name='inventory2'),
    path('wishlist/', views.wishlist, name='wishlist2'),
    path('search/', views.search, name='search2'),
    path('borrow_books/', views.borrow_books, name='borrow_books2'),
    path('logout/', views.logout_view, name='logout2'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('wishlist/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
    path('remove_from_wishlist/<int:book_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('get-random-books/', views.get_random_books, name='get_random_books2'),
    path('get-random-quote/', views.get_random_quote, name='get_random_quote2'),
    path('get-book-details/', views.get_book_details, name='get_book_details2'),
]