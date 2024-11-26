from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
def home(request):
    return render(request, 'home.html')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('student_success')  # Redirect after successful submission
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def student_success(request):
    return render(request, 'student_success.html')


def about(request):
    return render(request, 'about.html')


def students_list(request):

    students = Student.objects.all()  # Fetch all students from the database

    return render(request,'students_list.html', {'students': students})
