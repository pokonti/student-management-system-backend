from django.db import models

from courses.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    phone = models.CharField(max_length=15, blank=True)
    courses = models.ManyToManyField("courses.Course", related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30) 
    phone = models.CharField(max_length=15, blank=True)
    # courses = models.ManyToManyField("courses.Course", related_name="teachers")



    def __str__(self):
        return f"{self.first_name} {self.last_name}"




