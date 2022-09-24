from django.db import models
import os

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="homepage/img")
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.title
