from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

from django.urls import reverse
from ckeditor.fields import RichTextField





class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all_blogs')


class Blog(models.Model):

    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    description = RichTextField(null = True)
    date = models.DateTimeField(auto_now_add=True)
    
    

    def __unicode__(self):
        return self.title + '|' + self.author

    def get_absolute_url(self):
        return reverse('all_blogs')