from django.db import models


class Message(models.Model):
    """
    Stores a single contact message.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    read = models.BooleanField(default=False)
