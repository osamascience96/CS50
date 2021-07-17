from django.db import models

# Create your models here.
class Prophet(models.Model):
    full_name = models.CharField(max_length=64)
    speciality = models.CharField(max_length=64)
    age = models.IntegerField()
    details = models.TextField()