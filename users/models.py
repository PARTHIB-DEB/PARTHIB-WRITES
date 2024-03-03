from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.db import models

class newUserManager(BaseUserManager):
    def create_user(self, username, email, password):
        """
        Overring this method - it just makes a normal user / customer.
        """
        username = "".join(str(username).split(" "))
        email = "".join(str(email).split(" "))
        password = "".join(str(password).split(" "))
        
        if not username:
            raise ValueError("Must have one Username")
        
        if not email:
            raise ValueError("Must have one Email")
        
        if not password:
            raise ValueError("Must have one Password")
        

        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email ,password):
        """
        Overring this method - it just makes a Superuser.
        """
        
        username = "".join(str(username).split(" "))
        email = "".join(str(email).split(" "))
        password = "".join(str(password).split(" "))
        
        if not username:
            raise ValueError("Must have one UNIQUE Username")
        
        if not email:
            raise ValueError("Must have one Email")
        
        if not password:
            raise ValueError("Must have one UNIQUE Password")
        

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            password = password,
            is_staff = True,
            is_superuser = True,
            is_active = True,
        )
        user.is_admin =True
        user.save(using=self._db)
        return user


class newUser (AbstractUser):
    
    '''
    This Model is used to redefine the User model. Although the User model already consists these fields,
    but UserCreationForm default takes 'username' , 'password1' , 'password2'. That's why , Overriding of these
    fields is happenning.
    '''

    first_name=models.CharField()
    last_name=models.CharField()
    email = models.EmailField(unique=True)
    
    REQUIRED_FIELDS = ["email"]
    
    objusers = newUserManager()
    # objects = newUserManager()
    
    def __str__(self) -> str:
        return self.username