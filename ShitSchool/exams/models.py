from datetime import datetime
from django.db import models
 
# Create your models here.
 
class Exam(models.Model):
    name = models.CharField(max_length=64)
    deadline = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=64)
