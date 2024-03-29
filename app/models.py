from django.db import models
import datetime
from django.utils import timezone


from django.contrib.auth.models import AbstractUser


# Create your models here.


# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(null=True, unique=True)
#     bio = models.TextField(null=True)
    
#     avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

    

class Question(models.Model): 
    question_text = models.CharField(max_length=200) 
    pub_date = models.DateTimeField('date published')

    def __str__(self): 
        return self.question_text

def was_published_recently(self): 
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    # choice_correct = models.CharField(max_length=200) 
    votes = models.IntegerField(default=0)

    def __str__(self): 
        return self.choice_text

    

    