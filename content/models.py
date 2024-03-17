from django.db import models
from django.utils.text import slugify
from blog.settings import AUTH_USER_MODEL

# Create your models here.

class articleCreateModel(models.Model):
    
    '''
    This Model is Used to do CRUD operations on blogs. That means this model is entirely
    dedicated to blog-writer's Tasks. So it is the PARENT MODEL / PARENT TABLE.
    '''
    
    title = models.CharField(unique=True,max_length=60) # Blog Title
    catchline = models.TextField(unique=True,max_length=60) # Blog Catchline
    thumbnail = models.ImageField(upload_to="") # Blog Thumbnail
    script = models.CharField(unique=True) # Blog Content
    
    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        self.title=slugify(self.title)
        super(articleCreateModel,self).save(*args, **kwargs)

class articleViewModel(models.Model):
    
    '''
    This Model is used to navigate VIEWER'S INTERACTIONS with the blogs. So it is the CHILD MODEL , dependent on
    its PARENT MODEL. Now ONE blog can be watched and reviewed by MANY viewers, 
    that's why it has a 1-to-M relationship.
    
    But this table has some interesting - it has 2 PARENT - NewUser and articleViewModel. why?
    Because , only if the USER EXISTS (will locate the username in the parent) and BLOG EXISTS (will locate the blog in the parent)
    then this Model will work
    '''
    
    CHOICES = (
        ('LIKE',1),
        ('-----',0)
    )
    
    btitle_id = models.ForeignKey(articleCreateModel,null=True, blank = True, on_delete=models.CASCADE , db_column="btitle_id") # The blog , identified by BLOG-TITLE
    btitle = models.CharField()
    total_likes=models.IntegerField(default=0)  # Total Liked the blog got (numbers)
    total_comments = models.IntegerField(default=0)  # Total Comments the blog got (numbers)
    per_comment = models.CharField(null=True,blank=True) # Individual Comment of viewers
    per_like = models.IntegerField(null=True,blank=True,choices=CHOICES,default=0) # Individual Like of viewers
    username = models.CharField(null=True, blank = True)
    user_id = models.ForeignKey(AUTH_USER_MODEL, null=True, blank = True, on_delete=models.CASCADE , db_column="user_id") # Viewer's identity , got by USERNAME
    
    def __str__(self) -> str:
        return self.username

