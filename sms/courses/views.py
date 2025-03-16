from rest_framework import generics
from rest_framework.response import Response
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from users.serializers import StudentSerializer
from users.models import Student
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentsByCourseView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']  # Get course ID from URL
        return Student.objects.filter(courses__id=course_id)
    

class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonStudentsView(generics.ListAPIView):
    """Retrieve students enrolled in a specific lesson"""
    
    serializer_class = StudentSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        try:
            lesson = Lesson.objects.get(pk=pk)
            return lesson.students.all()  
        except Lesson.DoesNotExist:
            return Student.objects.none() 