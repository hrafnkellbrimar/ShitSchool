from datetime import datetime
from django.db import models
 
# Create your models here.
 
class Exam(models.Model):
    name = models.CharField(max_length=64)
    deadline = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=64)

class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.CharField(max_length=256)
    position = models.IntegerField()
    value = models.IntegerField()

class Results(models.Model):
    exam_name = models.ForeignKey(Exam)
    score = models.IntegerField()
    #student_name
