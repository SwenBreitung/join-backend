

from django.db import models
import datetime
from django.conf import  settings
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=30)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def time_past(self):
      today = datetime.date.today()
      data = today - self.created_at
      return data.days
    