from django.contrib.auth import get_user_model
from django.db import models

from news.models import New

User = get_user_model()

# Create your models here.
from simpleblog.serializers import UsersSerializer


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    news = models.ForeignKey(New, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='answers', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_answers(self):
        if self.answers.exists():
            return [instance.get_data() for instance in self.answers.all()]
        return None

    def get_data(self):
        return {
            'id': self.id,
            'owner': UsersSerializer(self.owner).data,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'answers': self.get_answers()
        }
