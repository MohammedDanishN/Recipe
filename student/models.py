from django.db import models

# Create your models here.


class StudentID(models.Model):
    srn = models.CharField(max_length=20)

    def __str__(self):
        return self.srn


class Department(models.Model):
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ['department']


class Student(models.Model):
    srn = models.OneToOneField(StudentID, on_delete=models.CASCADE)
    dept_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=18)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Subject(models.Model):
    subject_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.subject_name


class SubjectMarks(models.Model):
    student = models.ForeignKey(
        Student, related_name="student_marks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(default=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.student.name} | {self.subject.subject_name}'

    class Meta:
        unique_together = ['student', 'subject']
