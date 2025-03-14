from django.urls import path
from .views import CourseListCreateView, CourseDetailView, StudentsByCourseView, LessonListCreateAPIView, LessonDetailView, LessonStudentsView
urlpatterns = [
    path('', CourseListCreateView.as_view()),
    path('<int:pk>/', CourseDetailView.as_view()),
    path('<int:pk>/students/', StudentsByCourseView.as_view()),
    path('lessons/', LessonListCreateAPIView.as_view()),
    path('lessons/<int:pk>/', LessonDetailView.as_view()),
    path('lessons/<int:pk>/students/', LessonStudentsView.as_view()),
]

