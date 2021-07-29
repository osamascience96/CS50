from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=64)
    link = models.TextField()    