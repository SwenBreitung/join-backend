from django.db import models
import datetime
from django.conf import  settings
from django.contrib.auth.models import User
# Create your models here.



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    time = models.CharField(max_length=5)  # Angenommen, dieses Format ist HH:MM
    date = models.CharField(max_length=10) # Angenommen, dieses Format ist YYYY-MM-DD
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Subtask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    


class Contact(models.Model): 
    task = models.ForeignKey(Task, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

# Create your models here.
