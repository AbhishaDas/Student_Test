from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_key         = models.CharField(max_length=10, unique=True)
    subject_name        = models.CharField(max_length=100)
    
    def __str__(self):
        return self.subject_name
    
    
class Student(models.Model):
    student_key         = models.CharField(max_length=10, unique=True)
    student_name        = models.CharField(max_length=100)
    subject             = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade               = models.FloatField()
    remarks             = models.CharField(max_length=10)
    
    def save(self, *args, **kwargs):
        if self.grade >= 75:
            self.remarks = "PASS"
        else:
            self.remarks = "FAIL"
        super().save(*args, **kwargs)

        
    def __str__(self):
        return self.student_name