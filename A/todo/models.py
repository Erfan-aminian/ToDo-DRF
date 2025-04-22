from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todo')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.is_completed}"

