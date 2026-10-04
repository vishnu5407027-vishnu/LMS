# Mini LMS (Learning Management System)

A backend-driven web application built with Django and Django REST Framework featuring JWT Authentication and a modern, sleek UI.

## Features
- **User Authentication**: Secure Login/Register via JWT.
- **Role-Based Access**: Admin, Instructor, and Student roles.
- **Course Management**: Create and manage courses and lessons.
- **Assignment System**: Instructors create assignments; Students submit them.
- **Modern Dashboard**: Responsive UI with dark mode and vibrant accents.

## Setup Instructions

To run this project on another machine, follow these steps:

### 1. Clone or Copy the Project
Ensure you have the project files on your machine.

### 2. Set Up Virtual Environment
Open your terminal in the project root directory and run:
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 4. Database Migrations
Initialize the SQLite database and create tables:
```powershell
python manage.py makemigrations accounts courses
python manage.py migrate
```

### 5. Create a Superuser (Optional)
To access the Django Admin panel:
```powershell
python manage.py createsuperuser
```

### 6. Run the Development Server
```powershell
python manage.py runserver
```
The application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints
- `POST /api/accounts/register/` - Register
- `POST /api/accounts/login/` - Login (Obtain JWT)
- `GET /api/courses/list/` - List Courses
- `POST /api/courses/submissions/` - Submit Assignment

## Built With
- **Python/Django** - Backend Framework
- **Django REST Framework** - API Layer
- **SimpleJWT** - Authentication
- **Vanilla CSS** - Frontend Styling
- **JavaScript (Fetch API)** - Frontend Logic
