from django.db import models
from .user_model import User

class CommunityPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=SET_NULL)
        
    def __str__(self):
           return self.title