from django.db import models
from user.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}: {self.message}'


class Prompt(models.Model):
    prompt = models.CharField(max_length=1000)

    def __str__(self):
        return self.prompt[:50]
