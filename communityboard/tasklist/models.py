from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
