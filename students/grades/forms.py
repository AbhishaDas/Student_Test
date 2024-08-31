
from django import forms
from .models import Student, Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_key', 'student_name', 'subject', 'grade']
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_key', 'subject_name']
        