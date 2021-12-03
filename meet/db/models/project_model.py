from django.db import models

class UserProjects(models.Model):
    STATE = [
        ('Completed', 'Completed'),
        ('Ongoing', 'Ongoing')
    ]
    owner = models.OneToOneField(User)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    project_url = models.URLField()
    status = models.CharField(max_length=15, choices=STATE)
    
    