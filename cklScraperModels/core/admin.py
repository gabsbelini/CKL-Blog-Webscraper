from django.contrib import admin
from .models import Subject, Author


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    search_fields = ['name']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Author, AuthorAdmin)
