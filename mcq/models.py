from django.db import models
from core.models import Teacher, Subject, Class
from django import forms
import sys
from django.urls import reverse

# Create your models here.


class Assessment(models.Model):
    """Assessment class."""
    
    title = models.CharField(verbose_name='Assessment type', max_length=30)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_owner = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Academic Session', max_length=30)
    #questions = models.ManyToManyField('Question', blank=True)

    def filename(self):
        return str(self.name)
    
    def __str__(self) -> str:
        return str(self.name) + ' - ' + str(self.title) + ' ' + str(self.subject) + ' ' + str(self.class_owner)

    def get_absolute_url(self):
        return reverse('mcq:assessment', kwargs={'id' : self.id})


class Question(models.Model):
    """A class to generate questions"""

    # image directory to save images
    image_dir = 'Images/'
    image_folder_name = Assessment().filename()

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.TextField()
    # options = models.TextField()
    # correct_answer = models.CharField(max_length=200)

    DIR = image_dir + str(image_folder_name)
    upload = models.ImageField(verbose_name='Image upload', upload_to=DIR, blank=True)

    def __str__(self) -> str:
        return str(self.question)


class Option(models.Model):
    #assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_tag = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(verbose_name='Options', max_length=100)

    def __str__(self) -> str:
        return str(self.text)

class Answer(models.Model):
    #assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question_number = models.ForeignKey(Question, on_delete=models.CASCADE)
    # option = models.ForeignKey(Option, on_delete=models.CASCADE)
    answer = models.CharField(verbose_name='Correct answer', max_length=100)

    def __str__(self) -> str:
        return str(self.answer)