from django.urls import path
from . import views

urlpatterns = [
    # AUTH
    path('signin/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # DASHBOARD
    path('', views.dashboard, name='dashboard'),


    # ---------- STUDENTS ----------
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),

    # ---------- COURSES ----------
    path('courses/', views.course_list, name='course_list'),
    path('courses/delete/<int:id>/', views.delete_course, name='delete_course'),
]










