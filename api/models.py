import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    in_charge = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='in_charge')
    drafter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='drafter')
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
