from django.db import models
from django_markdown.models import MarkdownField

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=200)
    body=MarkdownField()
    p_date=models.DateTimeField(auto_now_add=True)
    youvid=models.URLField(blank=True)
    modified=models.DateTimeField(auto_now=True)
    desc=models.TextField(blank=True)

    def __str__(self):
        return self.title
