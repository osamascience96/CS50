from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
class Chat(models.Model):
    userId = models.ForeignKey(User, on_delete=CASCADE, null=True, related_name='user_reference')
    chatThread = models.TextField()


