# Generated by Django 5.1.7 on 2025-03-14 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        ("users", "0008_teacher"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="courses",
            field=models.ManyToManyField(related_name="teachers", to="courses.course"),
        ),
        migrations.AlterField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(related_name="students", to="courses.course"),
        ),
    ]
