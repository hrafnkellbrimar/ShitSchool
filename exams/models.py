from datetime import datetime
from django.db import models
from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
 
ANSWER_CHOICES = (('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'))
 
class Exam(models.Model):
    name = models.CharField(max_length=64)
    deadline = models.DateTimeField(default=datetime.now())
    author = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.CharField(max_length=256)
    position = models.IntegerField() # number of question in an exam
    solution = models.IntegerField() # an answer proposed by student
    answer = models.IntegerField() # the correct answer

class Results(models.Model):
    exam_name = models.ForeignKey(Exam)
    score = models.IntegerField()

class Options(models.Model): # Possible Answers to multiple choice questions
    answers = models.ManyToManyField(ExamQuestion)
    """
    one = models.CharField(max_length=256)
    two = models.CharField(max_length=256)
    three = models.CharField(max_length=256)
    four = models.CharField(max_length=256)
    """
class Theachers(models.Model):
    name = models.CharField(max_length=32)
    is_teacher = models.BooleanField()

class ExamForm(ModelForm):
    class Meta:
        model = Exam

class QuestionForm(ModelForm):
    class Meta:
        model = ExamQuestion

class OptionForm(ModelForm):
    class Meta:
        model = Options
