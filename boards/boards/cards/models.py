from django.db import models
from django.contrib.auth.models import User


class Card(models.Model):
    title = models.CharField(max_length=30, default="")
    info = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user', null=True, )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']