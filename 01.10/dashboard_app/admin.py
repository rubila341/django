from django.contrib import admin
from dashboard_app.models import Project, Task, Tag, ProjectFile
# Register your models here.






@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'display_count_of_files']
    search_fields = ['name']

    def display_count_of_files(self, obj):
        return obj.count_of_files
    display_count_of_files.short_description = 'Count of Files'



    def replace_spaces_with_underscore(self, request, objects):
        for i in objects:
            i.name = i.name.replace(' ', '_')
            i.save()
        return objects

    replace_spaces_with_underscore.short_description = 'Replace spaces with underscores'
    actions = ['replace_spaces_with_underscore']









@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'project', 'status', 'priority', 'created_at']
    search_fields = ['title']
    list_filter = ['status', 'priority', 'project', 'created_at']

    def change_status_closed(self, request, objects):
        for i in objects:
            i.status = 'Closed'
            i.save()
        return objects

    change_status_closed.short_description = 'Change status to closed'



    def change_status_pending(self, request, objects):
        for i in objects:
            i.status = 'Pending'
            i.save()
        return objects




    def change_priority_to_low(self, request, objects):
        for i in objects:
            i.priority = 'Low'
            i.save()
            return objects

    change_priority_to_low.short_description = 'Change priority to Low'

    def change_priority_to_medium(self, request, objects):
        for i in objects:
            i.priority = 'Medium'
            i.save()
            return objects

    change_priority_to_medium.short_description = 'Change priority to Medium'

    actions = ['change_priority_to_low', 'change_priority_to_medium', 'change_status_closed', 'change_status_pending']







@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']





@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
     ...




