from django.db import models

# Create your models here.
class Novel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=260)
