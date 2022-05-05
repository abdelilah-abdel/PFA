from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self) :
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(category , on_delete=models.SET_NULL , null=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self) :
        return self.name


class questions(models.Model):
    description = models.CharField(max_length=50)
    Quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.description



class reponse(models.Model):
    description = models.CharField(max_length=50)
    questions = models.OneToOneField(questions , on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.description