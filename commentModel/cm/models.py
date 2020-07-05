from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

class Comment(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    comment_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parentcom')

    def __str__(self):
        return self.content
    