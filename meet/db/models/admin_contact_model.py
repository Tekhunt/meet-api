from django.db import models

class ContactAdmin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    
    class Meta:
        verbose_name_plural = 'ContactAdmin'
        
    def __str__(self):
        return self.name
