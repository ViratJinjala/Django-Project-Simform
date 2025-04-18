from django.urls import path
from .views import (
    SubjectCreateView, SubjectDeleteView, SubjectUpdateView,
    ChapterCreateView, ChapterDeleteView, ChapterUpdateView,
    QuizCreateView, QuizDeleteView, QuizUpdateView,
    QuestionCreateView, QuestionDeleteView, QuestionUpdateView
)

urlpatterns = [
    path('subjects/create/', SubjectCreateView.as_view(), name='subject-create'),
    path('subjects/delete/<int:pk>/', SubjectDeleteView.as_view(), name='subject-delete'),
    path('subjects/update/<int:pk>/', SubjectUpdateView.as_view(), name='subject-update'),
    path('chapters/create/', ChapterCreateView.as_view(), name='chapter-create'),
    path('chapters/delete/<int:pk>/', ChapterDeleteView.as_view(), name='chapter-delete'),
    path('chapters/update/<int:pk>/', ChapterUpdateView.as_view(), name='chapter-update'),
    path('quizzes/create/', QuizCreateView.as_view(), name='quiz-create'),
    path('quizzes/delete/<int:pk>/', QuizDeleteView.as_view(), name='quiz-delete'),
    path('quizzes/update/<int:pk>/', QuizUpdateView.as_view(), name='quiz-update'),
    path('questions/create/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/delete/<int:pk>/', QuestionDeleteView.as_view(), name='question-delete'),
    path('questions/update/<int:pk>/', QuestionUpdateView.as_view(), name='question-update'),
]
