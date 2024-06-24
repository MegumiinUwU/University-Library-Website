# University Library System

## Introduction

Welcome to the University Library System! This web application is designed to manage book inventories, user profiles, borrowing and wishlist functionalities, and more. Our platform provides a seamless and user-friendly experience for both users and administrators, ensuring efficient management of books and user data. Whether you are a book lover looking to manage your reading list or an admin trying to maintain a vast collection of books, this system caters to all your needs.

## Features
### User Features
- **Sign Up and Log In**: Users can sign up and log in to their accounts. The system uses cookies to retrieve data specific to each user, including their borrowed books, wishlist, and profile.
- **Profile Management**: Users can view and edit their profile information, including profile picture, name, password, and date of birth. Editing requires authentication via password entry to ensure security.
- **Borrow Books**: Users can borrow books with appropriate exception handling to manage borrowing conflicts.
- **Wishlist**: Users can add books to their wishlist for future reference.
- **Book Search**: Users can search for books by name, author, description, or genre.
- **Paginator**: A paginator is implemented to display only 10 books per page with navigation buttons for next and last pages. This is used in viewing, borrowing, and editing books.
- **Category Filter**: Books can be filtered by category for easy browsing.
- **Random Quotes**: A random quote is displayed on top of the view books page, fetched from an API.
- **Dark Mode**: Users can switch to dark mode, which is saved across sessions using local storage.

### Admin Features
- **Sign Up and Log In**: Admins can sign up and log in to their accounts. The system uses cookies to retrieve data specific to each admin, including their profile and admin functionalities.
- **Profile Management**: Admins can view and edit their profile information, including profile picture, name, password, and date of birth. Editing requires authentication via password entry to ensure security.
- **Book Inventory Management**: Admins can manage the book inventory without using Django’s built-in admin panel. They can add, edit, and delete books.
- **Book Editing via AJAX**: Admins can edit book details dynamically using AJAX for a smooth and responsive experience.
- **Paginator**: A paginator is implemented to display only 10 books per page with navigation buttons for next and last pages. This is used in viewing, borrowing, and editing books.
- **Category Filter**: Books can be filtered by category for easy browsing.
- **Book Search**: Admins can search for books by name, author, description, or genre.
- **Dynamic Book Display**: Each time the home page is refreshed, different books are displayed using AJAX.
- **Random Quotes**: A random quote is displayed on top of the view books page, fetched from an API.
- **Dark Mode**: Admins can switch to dark mode, which is saved across sessions using local storage.
