from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer, UserListSerializer, RegisterUserSerializer
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework import status

# Эндпоинт для получения списка пользователей
class UserListGenericView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

# Эндпоинт для получения информации о конкретном пользователе
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Переопределим get_object, чтобы возвращать информацию о пользователе"""
        try:
            return User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist:
            raise NotFound("User not found")

# Эндпоинт для регистрации нового пользователя
class RegisterUserGenericView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = []  # Регистрация не требует аутентификации
    authentication_classes = []  # Регистрация не требует аутентификации

    def perform_create(self, serializer):
        """Выполняем создание пользователя"""
        serializer.save()

# Эндпоинт для работы с задачами (создание и получение)
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # При создании задачи сохраняем владельца
        serializer.save(owner=self.request.user)

# Эндпоинт для работы с подзадачами (создание и получение)
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # При создании подзадачи сохраняем владельца
        serializer.save(owner=self.request.user)

# Эндпоинт для получения и изменения задачи (по ID)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

# Эндпоинт для получения и изменения подзадачи (по ID)
class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
