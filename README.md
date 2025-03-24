

# Library Management System

Welcome to the **Library Management System** built with Django and MySQL! This project allows an admin to manage books (create, read, update, and delete) and provides a student view for browsing the book collection. Whether you're an admin with a passion for organization or a student looking for your next great read, this system has you covered.

---

## Features

- **Admin Signup/Login**  
  - Create an admin account with a unique email (no duplicates allowed!)
  - Login securely using your email and password
- **Book Management (CRUD)**
  - Add a new book entry
  - Update existing book information
  - Delete a book entry
  - Retrieve and view all book records
- **Student View**
  - Browse the library's collection without the admin overhead

---

## Project Structure

Here's how the project is structured:

```markdown
library_management/                  # Root project directory
├── manage.py                        # Django management script
├── library_management/              # Main project folder with settings
│   ├── __init__.py
│   ├── settings.py                  # Global settings (including MySQL configuration)
│   ├── urls.py                      # Root URL configuration
│   └── wsgi.py                     # WSGI configuration for deployment
├── library_app/                     # Application handling library functionalities
│   ├── __init__.py
│   ├── admin.py                     # Register models with Django admin
│   ├── apps.py                      # App configuration file
│   ├── models.py                    # Database models: Book, Admin (using Django's auth)
│   ├── views.py                     # Views for handling requests
│   ├── forms.py                     # (Optional) Custom forms for admin and book operations
│   ├── urls.py                      # App-specific URL routes
│   ├── templates/                   # HTML templates for the front end
│   │   └── library_app/
│   │       ├── base.html            # Base template (common layout)
│   │       ├── admin_signup.html    # Admin signup page
│   │       ├── admin_login.html     # Admin login page
│   │       ├── book_form.html       # Form for adding/updating a book
│   │       ├── book_list.html       # List of all books
│   │       └── ...                  # Other templates as needed
│   ├── static/                      # Static files: CSS, JavaScript, images
│   │   └── library_app/
│   │       ├── css/
│   │       ├── js/
│   │       └── images/
│   └── tests.py                     # Unit/integration tests for your app
└── requirements.txt                 # List of project dependencies (Django, mysqlclient, etc.)
```

---

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://your-repo-url.git
cd library_management
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv env
env\Scripts\activate  # On Windows
# For macOS/Linux use: source env/bin/activate
```

### 3. Install Dependencies

Install all required dependencies using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

In `library_management/settings.py`, update the `DATABASES` configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',            
        'USER': 'your_mysql_username',     
        'PASSWORD': 'your_mysql_password', 
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Make sure you have created the MySQL database (`library_db`) before proceeding.

### 5. Run Migrations

Create the database tables by running:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see your application in action!

---

## Testing

Testing is essential to ensure that our functionalities work as expected. You can run the tests using Django’s built-in test runner.

### 1. Example Test (in `library_app/tests.py`)

Here's an example test for the `Book` model:

```python
from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        # Create a sample book for testing
        self.book = Book.objects.create(
            title="Django for Beginners",
            author="John Doe",
            isbn="1234567890123"
        )

    def test_book_str_method(self):
        # Inline documentation: Ensure the __str__ method returns the book title.
        self.assertEqual(str(self.book), "Django for Beginners")
```

### 2. Run Tests

To run your tests, execute:

```bash
python manage.py test
```

This command will search for tests in your project and execute them. Make sure you write tests for admin functions, view responses, and form validations as you add those features.

---

## Code Documentation

We have added inline documentation (comments) throughout the code, particularly in critical areas like views, models, and tests. This ensures that anyone reading the code can understand the purpose and functionality of each part without needing a manual for every function.

Example in `views.py`:

```python
def book_list(request):
    """
    Retrieve all books from the database and render the book_list template.
    
    Returns:
        HttpResponse: A rendered page displaying all book entries.
    """
    books = Book.objects.all()  # Fetch all book records
    return render(request, 'library_app/book_list.html', {'books': books})
```

---

## Final Note

Thanks for checking out our project! We take our coding as seriously as our humor. So, tell us – when will we meet for coffee? I promise my humor's as strong as my debugging skills, and remember to **stay hydrated**!

Happy coding!
