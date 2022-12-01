from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.urls import reverse






class Category(models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all_blogs')

class Comments(models.Model):
    pass

class Blog(models.Model):

    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='blog', default='/blog/default.png')
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    
    


    def __str__(self):
        return f"{self.title} + '|' + {self.author}"

    def get_absolute_url(self):
        return reverse('all_blogs')