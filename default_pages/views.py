from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import validators
from .models import User, Book
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.urls import reverse
import requests
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'default_pages/home.html')

def home(request):
    return render(request, 'default_pages/home.html')

def search(request):
    query = request.POST.get('query', '')
    results = []

    if query:
        results = Book.objects.filter(
            Q(name__icontains=query) |
            Q(first_author__icontains=query) |
            Q(second_author__icontains=query) |
            Q(third_author__icontains=query) |
            Q(genre__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'default_pages/search.html', {'results': results})

from django.http import JsonResponse
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    response = render(request, 'user_pages/home.html')
                    response.set_cookie('user_email', email)
                    return response
                else:
                    messages.error(request, 'Invalid email or password')
            except User.DoesNotExist:
                messages.error(request, 'Invalid email or password')
        else:
            messages.error(request, 'Please enter both email and password')

    return render(request, 'default_pages/login.html')

def get_random_quote(request):
    
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    quote = data['content']
    return JsonResponse({'quote': quote})

import random
def get_random_books(request):
    # Retrieve all book objects from the database
    all_books = list(Book.objects.all())
    
    # Shuffle the list of books
    random.shuffle(all_books)
    
    # Select a subset of the shuffled list (e.g., the first 5 books)
    random_books = all_books[:3]
    
    # Prepare the data for JSON response
    books_data = [
        {
            'name': book.name,
            'first_author': book.first_author,
            'second_author': book.second_author,
            'third_author': book.third_author,
            'isbn': book.isbn,
            'publish_year': book.publish_year,
            'genre': book.genre,
            'description': book.description,
            'cover_image': book.cover_image.url if book.cover_image else None,
        }
        for book in random_books
    ]
    
    # Return the random books as JSON
    return JsonResponse({'books': books_data})


def get_book_details(request):
    name = request.GET.get('name')
    book = get_object_or_404(Book, name=name)
    book_data = {
        'name': book.name,
        'first_author': book.first_author,
        'second_author': book.second_author,
        'third_author': book.third_author,
        'isbn': book.isbn,
        'publish_year': book.publish_year,
        'genre': book.genre,
        'description': book.description,
        'cover_image': book.cover_image.url if book.cover_image else None,
    }
    return JsonResponse({'book': book_data})

import re

def custom_validate_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        return False
    
    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check if password contains at least one symbol
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        dob = request.POST['dob']
        country_code = request.POST['country_code']
        phone = request.POST['phone']

        # Validate password strength
        if not custom_validate_password(password):
            # messages.error(request, 'Password is not strong enough.')
            return render(request, 'default_pages/signup.html', {'error_message': 'Your password should be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character (such as !@#$%^&*).'})

        # Check if passwords match
        if password != confirm_password:
            # messages.error(request, 'Passwords do not match.')
            return render(request, 'default_pages/signup.html', {'error_message': 'Passwords do not match.'})
        if User.objects.filter(username=username).exists():
            # messages.error(request, 'Username already exists.')
            return render(request, 'default_pages/signup.html', {'error_message': 'Username already exists.'})
        # Create the user
        hashed_password = make_password(password)
        user = User(username=username, email=email, password=hashed_password)
        user.dob = dob
        user.country_code = country_code
        user.phone = phone
        user.save()

        # messages.success(request, 'Account created successfully.')
        return render(request, 'default_pages/signup.html', {'error_message': 'Account created successfully.'})

    return render(request, 'default_pages/signup.html')

def view_books(request):
    # Get the genre filter from the form if submitted
    genre = request.POST.get('category')

    # Query all books or filter by genre if provided
    if genre:
        books = Book.objects.filter(genre__icontains=genre)
    else:
        books = Book.objects.all()

    # Pagination
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'default_pages/view_books.html', {'page_obj': page_obj})
