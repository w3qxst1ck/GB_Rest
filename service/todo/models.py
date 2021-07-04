from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=128)
    users = models.ManyToManyField(User)
    repository = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.title


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project} - {self.user}'

