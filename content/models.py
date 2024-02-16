from django.db import models

# Create your models here.

class article(models.Model):
    title = models.TextField()
    script = models.CharField()
    likes=models.IntegerField()
    comments = models.IntegerField()
    per_comment = models.CharField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self) -> str:
        return self.title
