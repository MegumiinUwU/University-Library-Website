from django.db import models
import sys
import os
from django.contrib.auth.hashers import make_password,check_password
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from default_pages.models import User, Book # type: ignore 


class BorrowedBook(models.Model):
    user_email = models.EmailField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)  # Optional return date

    def __str__(self):
        return f'{self.user_email} borrowed {self.book.name}'

class Wishlist(models.Model):
    user_email = models.EmailField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user_email} added {self.book.name} to wishlist'
