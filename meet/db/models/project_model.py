from django.db import models
from .user_model import User
from .abstract_base_model import BaseModel


class UserProjects(models.Model, BaseModel):
    STATE = [
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing')
    ]
    owner = models.OneToOneField(User)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    project_url = models.URLField()
    status = models.CharField(max_length=15, choices=STATE)
