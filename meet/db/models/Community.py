from django.db import models
from django.db.models.deletion import SET_NULL
from .abstract_base_model import BaseModel
from .user_model import User
from .Community_project_model import CommunityProject
from .community_post_model import CommunityPost


class Community(models.Model, BaseModel):
    # user = models.ForeignKey(User, on_delete=SET_NULL)
    community_name = models.CharField(max_length=50)
    community_project = models.ForeignKey(CommunityProject)
    project_description = models.TextField(max_length=200)
    post = models.ForeignKey(CommunityPost)

    class Meta:
        verbose_name_plural = 'Communities'

    def __str__(self):
        return self.community_name
