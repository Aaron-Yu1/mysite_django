"""
This is define models.
Author: Aaron
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    """define a class for comment."""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "self.comment"


class Post(models.Model):
    """define a class for post."""
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "self.title"
