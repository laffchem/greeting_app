"""
Database models for greeting_app.
"""
from django.db import models
from model_utils.models import TimeStampedModel


class Greeting(models.Model):
    message = models.CharField(max_length=100)


    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return self.message
