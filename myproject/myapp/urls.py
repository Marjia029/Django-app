from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),  # Homepage URL
    path('about/', views.about, name='about'), # About
    path('add-student/', views.add_student, name='add_student'),  # Add student page
    path('student-success/', views.student_success, name='student_success'),  # Success page
    path('students/', views.students_list, name='students_list'),  # Students list page
]