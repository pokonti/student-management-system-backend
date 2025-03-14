from django.urls import path
from .views import StudentListCreateView, StudentDetailView, AddCourseToStudentView, RemoveCourseFromStudentView, TeacherListCreateView, TeacherDetailView

urlpatterns = [
    # path('users/', ),
    path('students/', StudentListCreateView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('teachers/', TeacherListCreateView.as_view()),
    path('teachers/<int:pk>/', TeacherDetailView.as_view()),
    path('students/<int:pk>/add_course/', AddCourseToStudentView.as_view()),
    path('students/<int:pk>/remove_course/', RemoveCourseFromStudentView.as_view())
]