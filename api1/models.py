from django.db import models
from django.contrib.auth.models import AbstractUser

# class BlogPost(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title 
class CustomUser(AbstractUser):
    pass