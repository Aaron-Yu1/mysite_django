"""
This is define that need to register.
Author: Aaron
"""

from django.contrib import admin
from .models import Post,Comment

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
