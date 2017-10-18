from django.db import models


class Subject(models.Model):
    name = models.CharField('Name', max_length=150)
    color = models.CharField('Color', max_length=20)


class Author(models.Model):
    name = models.CharField('Name', max_length=150)
    picture = models.ImageField(upload_to='pic_folder')
    
