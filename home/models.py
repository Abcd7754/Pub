from django.db import models

# Create your models here.
class Tasks(models.Model):
    TaskTitle = models.CharField(max_length=20);
    TaskDescription = models.CharField(max_length=100);
