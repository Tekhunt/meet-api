from django.db import models
from .user_model import User
from .abstract_base_model import BaseModel


class CommunityProject(models.Model, BaseModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    project_url = models.URLField()
    created_by = models.ForeignKey(User, )

    def __str__(self):
        return self.title
