from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from .project import Project
from .tag import Tag
from django.contrib.auth.models import User


STATUSES_CHOICES = [
    ('New', 'New'),
    ('In_progress', 'In_progress'),
    ('Completed', 'Completed'),
    ('Closed', 'Closed'),
    ('Pending', 'Pending'),
    ('Blocked', 'Blocked'),
]


PRIORITY_CHOICES = [
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('Very High', 'Very High'),
]

class Task(models.Model):
    title = models.CharField(
        max_length=255, unique=True, validators=[MinLengthValidator(10)]
    )
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUSES_CHOICES, default='New')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')  # NEW
    due_date = models.DateTimeField(null=True, blank=True)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering =  ['-due_date', '-priority']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        unique_together = (('title', 'project'),)

