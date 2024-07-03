from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    language_1 = models.PositiveIntegerField()
    language_2 = models.PositiveIntegerField()
    acting = models.PositiveIntegerField()
    dance = models.PositiveIntegerField()

    def __str__(self):
        return f"Subject Marks for {self.student.name}"