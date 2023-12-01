from django.db import models
from django.contrib.auth.models import User
  
#Create your models here.
class PublishedArticle(models.Model):
    todo = models.CharField(max_length=40)
    date = models.DateField(auto_now=True)