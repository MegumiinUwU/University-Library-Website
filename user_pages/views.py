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
from .models import BorrowedBook, Wishlist



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
            return render(request, 'user_pages/profile.html',{'User': None}) 
        
        if check_password(old_password,user.password):
            if new_password == confirm_password:
                if new_password:
                    user.password = make_password(new_password)
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
                response = render(request, 'user_pages/profile.html',{'User': user})
                response.set_cookie('user_email', newemail)
                return response
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Invalid old password.')
    if user:
        return render(request, 'user_pages/profile.html',{'User': user})
    return render(request, 'user_pages/profile.html',{'User': None})


def home(request):
    # Placeholder view function for the home page
    return render(request, 'user_pages/home.html')


def inventory(request):
    # Get user's email from cookies
    email = request.COOKIES.get('user_email')
    
    # Query the user's borrowed books
    borrowed_books = BorrowedBook.objects.filter(user_email=email)
    
    # Get the books associated with the borrowed books
    inventory = [borrowed_book.book for borrowed_book in borrowed_books]

    # Render the inventory template with the user's borrowed books
    return render(request, 'user_pages/inventory.html', {'inventory': inventory})

def return_book(request, book_id):
    if request.method == 'POST':
        # Get the book instance
        book = Book.objects.get(id=book_id)
        
        # Add the book back to the inventory
        book.quantity += 1
        book.save()
        borrowed_book = get_object_or_404(BorrowedBook, book=book)
        borrowed_book.delete()
        # Redirect to the inventory page with a success message
        return redirect('inventory2')
    else:
        # If the request method is not POST, redirect to the inventory page
        return redirect('inventory2')


def wishlist(request):
    # Get user's email from cookies
    email = request.COOKIES.get('user_email')
    
    # Query the user's wishlist
    wishlist_items = Wishlist.objects.filter(user_email=email)
    
    # Get the books associated with the wishlist items
    wishlist = [wishlist_item.book for wishlist_item in wishlist_items]

    # Render the wishlist template with the user's wishlist items
    return render(request, 'user_pages/wishlist.html', {'wishlist': wishlist})

def remove_from_wishlist(request, book_id):
    if request.method == 'POST':
        # Get the book instance
        book = get_object_or_404(Book, id=book_id)
        
        # Remove the book from the user's wishlist
        Wishlist.objects.filter(book=book, user_email=request.COOKIES.get('user_email')).delete()
        
        # Redirect to the wishlist page with a success message
        return redirect('wishlist2')
    else:
        # If the request method is not POST, redirect to the wishlist page
        return redirect('wishlist2')


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

    return render(request, 'user_pages/search.html', {'results': results})



def borrow_books(request):
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

    return render(request, 'user_pages/borrow.html', {'page_obj': page_obj})


def borrow_book(request, book_id):
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
        
    if request.method == 'POST':
        email = request.COOKIES.get('user_email')
        book = Book.objects.get(id=book_id)
        if BorrowedBook.objects.filter(user_email=email, book=book).exists():
           return render(request, 'user_pages/borrow.html', {'error_message': 'You have already borrowed this book.', 'page_obj': page_obj})
        if book.quantity > 0:
            BorrowedBook.objects.create(user_email=email, book=book)
            book.quantity -= 1
            book.save()
            return render(request, 'user_pages/borrow.html', {'error_message': 'Book borrowed successfully!', 'page_obj': page_obj})
        else:
            return render(request, 'user_pages/borrow.html', {'error_message': 'Book is out of stock!', 'page_obj': page_obj})

def add_to_wishlist(request, book_id):
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
        
    if request.method == 'POST':
        email = request.COOKIES.get('user_email')
        book = Book.objects.get(id=book_id)
        if Wishlist.objects.filter(user_email=email, book=book).exists():
            return render(request, 'user_pages/borrow.html', {'error_message': 'Book is already in your wishlist.', 'page_obj': page_obj})
        Wishlist.objects.create(user_email=email, book=book)
        return render(request, 'user_pages/borrow.html', {'error_message': 'Book added to wishlist successfully!', 'page_obj': page_obj})




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