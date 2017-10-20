from django.db import models


class Subject(models.Model):
    name = models.CharField('Name', max_length=150)
    color = models.CharField('Color', max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Name', max_length=150)
    picture = models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('Title', max_length=300)
    slug = models.CharField('Slug', max_length=100)
    author = models.ForeignKey('core.Author', verbose_name='Author Name')
    subject = models.ForeignKey('core.Subject', verbose_name='Subject')
    hero_image = models.ImageField(upload_to='pictures')
    publish_date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return self.title
