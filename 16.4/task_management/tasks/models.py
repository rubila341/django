from django.contrib.auth.models import User
from django.db import models

# Модель задачи
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Модель подзадачи
class SubTask(models.Model):
    title = models.CharField(max_length=255)
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Модель профиля пользователя (расширение User)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    project = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
