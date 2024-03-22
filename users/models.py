from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin, BaseUserManager
from django.db import models

class newUserManager(BaseUserManager):
    def create_user(self, username, email, password,**others):
        """
        Overring this method - it just makes a normal user / customer.
        """
        
        if not username:
            raise ValueError("Must have one Username")
        
        if not email:
            raise ValueError("Must have one Email")
        
        if not password:
            raise ValueError("Must have one Password")
        
        username = "".join(str(username).split(" "))
        email = "".join(str(email).split(" "))
        password = "".join(str(password).split(" "))
        
        others.setdefault('is_active',True)

        user = self.model(
            username = username,
            email=self.normalize_email(email),
            **others
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password,**others):
        """
        Overriding this method - it just makes a Superuser.
        """

        if not username:
            raise ValueError("Must have one UNIQUE Username")

        if not email:
            raise ValueError("Must have one Email")

        if not password:
            raise ValueError("Must have one UNIQUE Password")
        
        others.setdefault('is_staff', True)
        others.setdefault('is_superuser', True)
        
        return self.create_user(
            self,
            username, 
            email, 
            password, 
            **others
        )

    

class newUser (AbstractBaseUser,PermissionsMixin):
    
    '''
    This Model is used to redefine the User model. Although the User model already consists these fields,
    but UserCreationForm default takes 'username' , 'password1' , 'password2'. That's why , Overriding of these
    fields is happenning.
    '''
    username = models.CharField(primary_key=True)
    first_name=models.CharField(null=True,blank=True)
    last_name=models.CharField(null=True,blank=True)
    email = models.EmailField(unique=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email"
    ]
    
    objects = newUserManager()
    
    
    def __str__(self) -> str:
        return self.username