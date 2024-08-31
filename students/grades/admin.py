from django.contrib import admin
from .models import Subject, Student

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_key', 'subject_name']
    search_fields = ['subject_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_key', 'student_name', 'subject', 'grade', 'remarks']
    search_fields = ['student_name']
    list_filter = ['subject', 'remarks'] 
