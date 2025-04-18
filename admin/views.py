from rest_framework import generics, permissions
from users.models import Subject, Chapter, Quiz, Question
from users.serializers import SubjectSerializer, ChapterSerializer, QuizSerializer, QuestionSerializer


class SubjectCreateView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]

class SubjectDeleteView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]

class SubjectUpdateView(generics.UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]


class ChapterCreateView(generics.CreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.AllowAny]

class ChapterDeleteView(generics.DestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.AllowAny]

class ChapterUpdateView(generics.UpdateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [permissions.AllowAny]


class QuizCreateView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.AllowAny]

class QuizDeleteView(generics.DestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.AllowAny]

class QuizUpdateView(generics.UpdateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [permissions.AllowAny]


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]