from django.db import models

class ContactUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = 'ContactUser'
    
    def __str__(self):
        return self.name