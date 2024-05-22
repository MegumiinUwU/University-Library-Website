from django import forms
import sys
import os
from django.contrib.auth.hashers import make_password,check_password
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from default_pages.models import User, Book # type: ignore 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'first_author', 'second_author', 'third_author', 'isbn', 'publish_year', 'genre', 'cover_image']
