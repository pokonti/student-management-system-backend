# Generated by Django 5.1.7 on 2025-03-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_lesson"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
