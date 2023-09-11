"""
This is define app config.
Author: Aaron
"""

from django.apps import AppConfig


class BaseConfig(AppConfig):
    """Defined a class for app config."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
