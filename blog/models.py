from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class Post(models.Model):
    """Base fields of Post"""
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)

class Text(Post):
    """Text Post"""
    title = models.CharField(max_length=100)

class Photo(Post):
    """Photo Post"""
    image = models.ImageField(upload_to='blog_photo')

class Link(Post):
    """Link Post"""
    url = models.URLField()
