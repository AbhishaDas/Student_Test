from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/new/', views.student_create, name='student_create'),
    path('subject_create', views.subject_create, name='subject_create'),
    path('manage_student/<int:pk>', views.manage_student, name='manage_student')
]
