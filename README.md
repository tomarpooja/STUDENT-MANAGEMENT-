# Student Management App

A Django-based web app to manage students and courses efficiently with a clean dashboard.

## Features

- **Dashboard Overview:**  
  - Shows total students and total courses.
- **Student Management:**  
  - View all students with their name, email, and enrolled course.
  - Add new students using a form (name, email, course selection).
- **Course Management:**  
  - Add, view, and manage courses.
- **Authentication:**  
  - Student login and signup system.

## How to Run
```bash
git clone https://github.com/tomarpooja/STUDENT-MANAGEMENT-.git
cd crud                  # navigate to your project folder
python -m venv venv      # optional
venv\Scripts\activate    # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

