from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.core.files.storage import default_storage
from django.contrib import messages
import sys
import os
from django.contrib.auth.hashers import make_password,check_password
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from default_pages.models import User, Book # type: ignore 




def profile(request):
    # Get the user's email from the cookie
    email = request.COOKIES.get('user_email')
    user = User.objects.get(email=email)
    if request.method == 'POST':
        profile_picture = request.FILES.get('profilePicture')
        username = request.POST.get('username')
        old_password = request.POST.get('oldpassword')
        new_password = request.POST.get('newpassword')
        confirm_password = request.POST.get('confirmpassword')
        newemail = request.POST.get('email')
        phone_number = request.POST.get('phoneNumber')
        date_of_birth = request.POST.get('dateOfBirth')
        
        # Validate form fields here as needed
        
        # Fetch the user from the database
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
            return render(request, 'admin_pages/profile.html',{'User': None}) 
        
        if check_password(old_password,user.password):
            if new_password == confirm_password:
                if new_password:
                    user.set_password(new_password)
                user.username = username
                user.email =newemail
                user.phone = phone_number
                user.dob = date_of_birth
                if profile_picture:
                    file_name = default_storage.save(profile_picture.name, profile_picture)
                    # Update the user's profile picture
                    user.profile_picture = file_name
                user.save()
                messages.success(request, 'Your profile has been updated successfully!')
                response = render(request, 'admin_pages/profile.html',{'User': user})
                response.set_cookie('user_email', newemail)
                return response
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Invalid old password.')
    if user:
        return render(request, 'admin_pages/profile.html',{'User': user})
    return render(request, 'admin_pages/profile.html',{'User': None})


def home(request):
    # Placeholder view function for the home page
    return render(request, 'admin_pages/home.html')




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

    return render(request, 'admin_pages/search.html', {'results': results})

def addpage(request):
    return render(request, 'admin_pages/addpage.html')

def addbook(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        first_author = request.POST.get('author1')
        second_author = request.POST.get('author2')
        third_author = request.POST.get('author3')
        isbn = request.POST.get('ISBN')
        publish_year = request.POST.get('publishYear')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        cover_image = request.FILES.get('cover')
        
        # Validate form fields here as needed
        
        # Save the book to the database
        book = Book(
            name=name,
            first_author=first_author,
            second_author=second_author,
            third_author=third_author,
            isbn=isbn,
            publish_year=publish_year,
            genre=genre,
            description=description,
            cover_image=cover_image
        )
        book.save()
        
        messages.success(request, 'Book added successfully!')
        return render(request, 'admin_pages/addpage.html',{'error_message': 'Book added successfully!'})
    
    return render(request, 'admin_pages/addpage.html')

from .forms import BookForm


def admin_book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_pages/allbooks.html', {'page_obj': page_obj})

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

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.name = request.POST.get('name')
        book.first_author = request.POST.get('first_author')
        book.second_author = request.POST.get('second_author')
        book.third_author = request.POST.get('third_author')
        book.isbn = request.POST.get('isbn')
        book.publish_year = request.POST.get('publish_year')
        book.genre = request.POST.get('genre')
        book.description = request.POST.get('description')
        if 'cover_image' in request.FILES:
            book.cover_image = request.FILES['cover_image']
        book.quantity = request.POST.get('quantity')
        book.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})




def logout_view(request):
    # Delete the user's session data (cookie)
    response = render(request, 'default_pages/home.html') 
    response.delete_cookie('user_email')  
    return response

import requests
from django.http import JsonResponse
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



