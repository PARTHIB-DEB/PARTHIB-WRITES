from django.db import models
from django.contrib.auth.models import User
from content.models import *

# Create your models here.

class engagements(models.Model):
    username = models.ForeignKey(User,null=True,blank=True, related_name="uname",on_delete=models.CASCADE)
    likes = models.ForeignKey(article, null=True,blank=True, related_name="like", on_delete=models.CASCADE)
    comments = models.ForeignKey(article, null=True,blank=True, related_name="comment", on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.username