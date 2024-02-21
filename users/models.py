from django.contrib.auth.models import AbstractUser
from django.db import models

class newUser (AbstractUser):
    
    '''
    This Model is used to redefine the User model. Although the User model already consists these fields,
    but UserCreationForm default takes 'username' , 'password1' , 'password2'. That's why , Overriding of these
    fields is happenning.
    '''

    first_name=models.CharField()
    last_name=models.CharField()
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.username