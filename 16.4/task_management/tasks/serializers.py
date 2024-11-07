
from rest_framework import serializers
from .models import Task, SubTask, User

# Сериализатор для списка пользователей
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Сериализатор для регистрации нового пользователя
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

# Сериализатор для подзадач
class SubTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'status', 'owner', 'task', 'created_at', 'updated_at']

# Сериализатор для задач
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'owner', 'subtasks', 'created_at', 'updated_at']

# Ваши представления (views)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Task, SubTask, User
from .permissions import IsOwner

# Эндпоинт для получения списка пользователей
class UserListGenericView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserListSerializer

# Эндпоинт для получения информации о конкретном пользователе
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return UserListSerializer

    def get_object(self):
        """Переопределим get_object, чтобы возвращать информацию о пользователе"""
        try:
            return User.objects.get(id=self.kwargs['pk'])
        except User.DoesNotExist:
            raise NotFound("User not found")

# Эндпоинт для регистрации нового пользователя
class RegisterUserGenericView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []  # Регистрация не требует аутентификации
    authentication_classes = []  # Регистрация не требует аутентификации

    def get_serializer_class(self):
        return RegisterUserSerializer

    def perform_create(self, serializer):
        """Выполняем создание пользователя"""
        serializer.save()

# Эндпоинт для работы с задачами (создание и получение)
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return TaskSerializer

    def perform_create(self, serializer):
        # При создании задачи сохраняем владельца
        serializer.save(owner=self.request.user)

# Эндпоинт для работы с подзадачами (создание и получение)
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return SubTaskSerializer

    def perform_create(self, serializer):
        # При создании подзадачи сохраняем владельца
        serializer.save(owner=self.request.user)

# Эндпоинт для получения и изменения задачи (по ID)
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        return TaskSerializer

# Эндпоинт для получения и изменения подзадачи (по ID)
class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_serializer_class(self):
        return SubTaskSerializer
