from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject
from .forms import StudentForm, SubjectForm

def student_list(request):
    students = Student.objects.all()

    filter_value = request.GET.get('filter', 'all')
    if filter_value == 'pass':
        students = students.filter(remarks="PASS")
    elif filter_value == 'fail':
        students = students.filter(remarks="FAIL")

    search_query = request.GET.get('q')
    if search_query:
        students = students.filter(student_name__icontains=search_query)

    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def subject_create(request):
    subjects = Subject.objects.all()
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('subject_create')
    else:
        form = SubjectForm()
    
    return render(request, 'subject_form.html', {'subjects':subjects, 'form':form})


def manage_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('student_list')
        elif 'delete' in request.POST:
            student.delete()
            return redirect('student_list')
        else:
            form = StudentForm(instance=student)
    else:
        form = StudentForm(instance=student)

    return render(request, 'manage_student.html', {'student': student, 'form': form})