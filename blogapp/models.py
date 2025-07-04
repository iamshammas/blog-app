from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title