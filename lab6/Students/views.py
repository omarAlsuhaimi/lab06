from django.shortcuts import render
from django.db import models
from django import forms
from Students.models import Student,Course
from . import templates
# Create your views here.

def displayStudents(request):
    if request.method == "POST":
        student = StudentModelForm(request.POST)
        student.save()

    return render(request,"displayStudents.html",{"students":Student.objects.all(),"form": StudentModelForm()})
def displayStudentDetails(request,student_id):
    student = Student.objects.get(id=student_id)
    registered_courses = student.courses.all()
    not_registered_courses = Course.objects.all().exclude(pk__in=registered_courses.values_list('pk', flat=True))

    return render(request,"displayStudentDetails.html",{"student":student,"notRegisteredCoureses":not_registered_courses})

def displayCourses(request):
    if request.method == "POST":
        course = CourseModelForm(request.POST)
        course.save()

    return render(request,"displayCourses.html",{"courses":Course.objects.all(),"form": CourseModelForm()})



class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

