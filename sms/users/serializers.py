from rest_framework import serializers
from .models import Student, Teacher
from courses.serializers import CourseSerializer
from courses.models import Course



class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class AddCourseSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()

    def validate_course_id(self, value):
        """Check if the course exists"""
        if not Course.objects.filter(id=value).exists():
            raise serializers.ValidationError("Course not found")
        return value
    
class RemoveCourseSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()

    def validate_course_id(self, value):
        """Check if the course exists"""
        if not Course.objects.filter(id=value).exists():
            raise serializers.ValidationError("Course not found")
        return value