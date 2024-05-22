from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    dob = models.DateField()
    country_code = models.CharField(max_length=7)
    phone = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/',default='profile_pictures/PfP.jpg', null=True, blank=True)

class Book(models.Model):
    name = models.CharField(max_length=200)
    first_author = models.CharField(max_length=100)
    second_author = models.CharField(max_length=100, blank=True, null=True)
    third_author = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=13)
    publish_year = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/')
    quantity = models.PositiveIntegerField(default=1)  

    def __str__(self):
        return self.name

