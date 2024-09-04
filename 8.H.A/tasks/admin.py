from django.contrib import admin
from .models import Task, SubTask, Category, Comment, TimeEntry

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at')
    search_fields = ('title',)
    list_filter = ('status', 'categories')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'created_at')
    search_fields = ('title',)
    list_filter = ('status', 'task')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'created_at')
    search_fields = ('content',)
    list_filter = ('task', 'user')

@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'start_time', 'end_time', 'duration')
    search_fields = ('task__title', 'user__username')
    list_filter = ('task', 'user')
    fields = ('task', 'user', 'start_time', 'end_time')
