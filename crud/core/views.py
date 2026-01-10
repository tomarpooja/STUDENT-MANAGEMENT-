from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Student, Course


# ------------------------
# Dashboard
# ------------------------
@login_required(login_url='login')
def dashboard(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, 'core/dashboard.html', context)


# ------------------------
# Authentication
# ------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'core/login.html')


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return redirect('signup')

        User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        messages.success(request, "Signup successful. Please login.")
        return redirect('login')

    return render(request, 'core/signup.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ------------------------
# Student Views
# ------------------------
@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'core/student_list.html', {'students': students})


@login_required(login_url='login')
def add_student(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        Student.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            age=request.POST.get('age'),
            course_id=request.POST.get('course')
        )
        return redirect('student_list')

    return render(request, 'core/add_student.html', {'courses': courses})


@login_required(login_url='login')
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    courses = Course.objects.all()

    if request.method == 'POST':
        student.full_name = request.POST.get('full_name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.course_id = request.POST.get('course')
        student.save()
        return redirect('student_list')

    return render(request, 'core/edit_student.html', {
        'student': student,
        'courses': courses
    })


@login_required(login_url='login')
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')


# ------------------------
# Course Views
# ------------------------
@login_required(login_url='login')
def course_list(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST.get('name'))
        return redirect('course_list')

    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})


@login_required(login_url='login')
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')


