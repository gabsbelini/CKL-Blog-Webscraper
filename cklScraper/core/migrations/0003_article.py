# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('slug', models.CharField(max_length=100, verbose_name='Slug')),
                ('hero_image', models.ImageField(upload_to='pictures')),
                ('publish_date', models.DateField()),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Author', verbose_name='Author Name')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Subject', verbose_name='Subject')),
            ],
        ),
    ]
