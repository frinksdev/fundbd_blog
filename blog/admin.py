from django.contrib import admin
from .models import post
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
admin.site.register(post, MarkdownModelAdmin)
