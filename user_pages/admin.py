from django.contrib import admin

from .models import BorrowedBook, Wishlist


# Register your models here.
admin.site.register(BorrowedBook)
admin.site.register(Wishlist)