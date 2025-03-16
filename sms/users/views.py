from rest_framework import generics
from .models import Student, Teacher
from courses.models import Course
from .serializers import StudentSerializer, TeacherSerializer, AddCourseSerializer, RemoveCourseSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        student = Student.objects.get(id=response.data['id'])  # Get the created student

        # Associate courses with the student
        for course in request.data.get('courses', []):
            course_obj = get_object_or_404(Course, id=course['id'])
            student.courses.add(course_obj)

        # Serialize the updated student
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class AddCourseToStudentView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddCourseSerializer  # Include serializer_class

    def update(self, request, *args, **kwargs):
        student_id = kwargs.get("pk")  # Get student ID from URL
        serializer = self.get_serializer(data=request.data)  # Validate input

        if serializer.is_valid():
            try:
                student = Student.objects.get(id=student_id)
                course = Course.objects.get(id=serializer.validated_data["course_id"])
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

            student.courses.add(course)
            return Response({"message": "Course added successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RemoveCourseFromStudentView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RemoveCourseSerializer  # Include serializer_class

    def update(self, request, *args, **kwargs):
        student_id = kwargs.get("pk")  # Get student ID from URL
        serializer = self.get_serializer(data=request.data)  # Validate input

        if serializer.is_valid():
            try:
                student = Student.objects.get(id=student_id)
                course = Course.objects.get(id=serializer.validated_data["course_id"])
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

            # Check if the course is associated with the student
            if course not in student.courses.all():
                return Response({"error": "Course not found in student’s courses"}, status=status.HTTP_400_BAD_REQUEST)

            student.courses.remove(course)
            return Response({"message": "Course removed successfully"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

