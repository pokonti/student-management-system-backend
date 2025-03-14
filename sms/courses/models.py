from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="lessons")
    teacher = models.ForeignKey("users.Teacher", on_delete=models.CASCADE, related_name="lessons")
    students = models.ManyToManyField("users.Student", related_name="lessons")
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.name})"