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
- **Dynamic Book Display**: Each time the home page is refreshed, different books are displayed using AJAX.

### Admin Features
- **Sign Up and Log In**: Admins can sign up and log in to their accounts. The system uses cookies to retrieve data specific to each admin, including their profile and admin functionalities.
- **Profile Management**: Admins can view and edit their profile information, including profile picture, name, password, and date of birth. Editing requires authentication via password entry to ensure security.
- **Book Management**: Admins can manage the book stock without using Django’s built-in admin panel. They can add, edit, and delete books.
- **Book Editing via AJAX**: Admins can edit book details dynamically using AJAX for a smooth and responsive experience.
- **Paginator**: A paginator is implemented to display only 10 books per page with navigation buttons for next and last pages. This is used in viewing, borrowing, and editing books.
- **Category Filter**: Books can be filtered by category for easy browsing.
- **Book Search**: Admins can search for books by name, author, description, or genre.
- **Dynamic Book Display**: Each time the home page is refreshed, different books are displayed using AJAX.
- **Random Quotes**: A random quote is displayed on top of the view books page, fetched from an API.
- **Dark Mode**: Admins can switch to dark mode, which is saved across sessions using local storage.

## Exception Handling

Our University Library System is built with robust exception handling mechanisms to ensure a smooth and error-free user experience. Below are some key areas where exception handling is implemented:

- **Sign Up and Log In**: Proper error messages are displayed if the user enters incorrect login credentials or attempts to sign up with already registered email addresses. Passwords must meet security requirements; otherwise, users will see: "Your password should be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character (such as !@#$%^&*)."
- **Profile Management**: When editing profile details, the system checks for incorrect or incomplete data entries. Users are prompted to re-enter information if validation fails.
- **Borrow Books**: The system handles exceptions such as attempting to borrow a book that is already borrowed by another user or exceeding the borrowing limit.
- **Wishlist**: Users are notified if a book they attempt to add to their wishlist is already present.

## Frameworks and Technologies

### Backend
- **Django**: The primary web framework used for developing the backend of the application.

### Frontend
- **HTML/CSS**: Used for structuring and styling the web pages.
- **JavaScript**: Utilized for various interactive features including AJAX calls, dark mode toggling, and profile picture uploads.

### Database
- **SQLite**: The default database used for development purposes.

## Gallery

Here are some GIFs demonstrating the Style <u> (not the features) </u> of the University Library System:

Search
<img src="README IMAGES/SEARCH.gif" alt="Search for book" width="800px" />


View Books
<img src="README IMAGES/VIEW BOOKS.gif" alt="Search for book" width="800px" />

Login
<img src="README IMAGES/LOGIN.gif" alt="Search for book" width="800px" />

Change Profile Picture
<img src="README IMAGES/PROFILE.gif" alt="Search for book" width="800px" />

Dark Mode
<img src="README IMAGES/DARK MODE.gif" alt="Search for book" width="800px" />

and more ...

