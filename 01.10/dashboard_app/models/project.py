from django.db import models


class ProjectFile(models.Model):
    name = models.CharField(max_length=120)
    file = models.FileField(upload_to='projects/')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Project File'
        verbose_name_plural = 'Project Files'
        ordering = ['-created_at']

    def __str__(self):
        return self.name



class Project(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.ManyToManyField(ProjectFile, related_name='projects')



    @property
    def count_of_files(self):
        return self.file.count()




    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        unique_together = (('name', 'created_at'),)






