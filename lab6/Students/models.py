from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length = 15)
    course_code = models.CharField(max_length = 6)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    first = models.CharField(max_length = 15)
    last= models.CharField(max_length = 15)
    phone = models.IntegerField()
    courses = models.ManyToManyField(Course,blank = True,related_name = "students")

