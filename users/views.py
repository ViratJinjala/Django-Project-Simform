from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User, Subject, Chapter, Quiz, Question
from .serializers import UserSerializer, SubjectSerializer, ChapterSerializer, QuizSerializer, QuestionSerializer
from .tasks import send_email_task
from .permissions import IsAdminUserCustom
from django.template.loader import render_to_string

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Send email to registered user via celery
        email = [serializer.validated_data.get('email')]
        subject="Welcome to Quiz app"
        message="It's pleasure seeing you here."
        username = [serializer.validated_data.get('username')]
        data_username = {
            'username': username
        }
        html_message = render_to_string('email_template.html', data_username)

        # Celery called here
        send_email_task.delay(email,subject,message,html_message)
        return Response(serializer.data)

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.save()

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUserCustom]
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUserCustom]
    permission_classes = [permissions.AllowAny]

class SubjectCreateView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    # permission_classes = [IsAdminUserCustom]
    permission_classes = [permissions.AllowAny]

class ChapterCreateView(generics.CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    # permission_classes = [IsAdminUserCustom]
    permission_classes = [permissions.AllowAny]

class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    # permission_classes = [IsAdminUserCustom]
    permission_classes = [permissions.AllowAny]

class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAdminUserCustom]
    permission_classes = [permissions.AllowAny]

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]

class ChapterListBySubjectView(generics.ListAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Chapter.objects.filter(subject_id=subject_id)

class QuizListByChapterView(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        chapter_id = self.kwargs['chapter_id']
        return Quiz.objects.filter(chapter_id=chapter_id)

class QuestionListByQuizView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        return Question.objects.filter(quiz_id=quiz_id)


