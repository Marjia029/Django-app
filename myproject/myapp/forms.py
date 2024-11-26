from django import forms
from .models import Student
from .models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'mobile']  # Fields to include in the form


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']  # Fields to include in the form