from django.urls import path
from .views import (
    UserRegistrationView, UserProfileView, UserListView, UserDetailView,
    SubjectListView, ChapterListBySubjectView, QuizListByChapterView, QuestionListByQuizView
)

urlpatterns = [
    path('create/', UserRegistrationView.as_view(), name='user-create'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/chapters/', ChapterListBySubjectView.as_view(), name='chapter-list-by-subject'),
    path('chapters/<int:chapter_id>/quizzes/', QuizListByChapterView.as_view(), name='quiz-list-by-chapter'),
    path('quizzes/<int:quiz_id>/questions/', QuestionListByQuizView.as_view(), name='question-list-by-quiz'),
]
