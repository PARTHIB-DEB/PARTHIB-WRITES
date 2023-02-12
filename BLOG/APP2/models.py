from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=30)
    catch=models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)
    image=models.ImageField(upload_to='media/')
    details=models.TextField()
    
    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        self.title=slugify(self.title)
        super(Blog,self).save(*args, **kwargs)