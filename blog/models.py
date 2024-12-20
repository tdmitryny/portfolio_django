from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField # type: ignore



# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(default=timezone.now)
    content = HTMLField()
    slug = models.SlugField(max_length=200, blank=True)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title