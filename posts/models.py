from django.db import models


class Post(models.Model):
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    content = models.TextField()