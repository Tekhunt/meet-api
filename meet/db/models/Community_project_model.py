from django.db import models
from .user_model import User

class CommunityProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    project_url = models.URLField()
    created_by = models.ForeignKey(User)
        
    def __str__(self):
           return self.title