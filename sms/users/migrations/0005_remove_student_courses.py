# Generated by Django 5.1.7 on 2025-03-12 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_course_student_courses"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="courses",
        ),
    ]
