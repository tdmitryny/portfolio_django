from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=2000, blank=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title