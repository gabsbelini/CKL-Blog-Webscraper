from django.db import models


class Subject(models.Model):
    name = models.CharField('Name', max_length=150)
    color = models.CharField('Color', max_length=50)
    
