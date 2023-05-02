from django.db import models
from datetime import datetime
# Create your models here.

class Tasks(models.Model):
    Task_name = models.CharField(max_length=50)
    Description = models.TextField(blank=True)
    Date_and_Time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Task_name