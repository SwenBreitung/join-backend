from django.db import models
from tasks.models import Task


# class Contact(models.Model): 
#     # task = models.ForeignKey(Task, related_name='contacts', on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     color = models.CharField(max_length=100)
# Create your models here.
class IndependentContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    color = models.CharField (max_length = 20)