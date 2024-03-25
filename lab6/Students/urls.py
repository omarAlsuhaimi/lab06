from django.urls import path
from . import views
urlpatterns=[
    path("students/",views.displayStudents,name = "displayStudents"),
    path("<int:student_id>/",views.displayStudentDetails,name="displayStudentDetails"),
    path("courses/",views.displayCourses,name="displayCourses")


]