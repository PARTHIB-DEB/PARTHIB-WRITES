import pytest

from django.urls import reverse
from users.models import *
from dotenv import load_dotenv
import os

load_dotenv()

Sender_Email = os.getenv('EMAIL_HOST_USER')
Sender_Email_Password = os.getenv('EMAIL_HOST_PASSWORD')


# Testing will be done for these functions
# Signin (register)  , Signout (Delete) , Login , Logout , Likes and Comments (Probably)
# Probably a Class will be best for this case



supuser = {
  "username" : "Pkd",
  "email" : Sender_Email,
  "password" : Sender_Email_Password,
  "first_name" : "Parthib" , 
  "last_name" : "Kumar Deb"
}

normuser = {
  "username" : "Xyz",
  "email" : "Xyz@gmail.com",
  "password" : "Zk1234mp!",
  "first_name" : "Zetan" , 
  "last_name" : "Su"
}


@pytest.mark.django_db
def test_superuser_creation(client, django_user_model):
    user_obj = django_user_model.objects.create_superuser(
          username = supuser.get('username'),
          email = supuser.get('email'),
          password = supuser.get('password'),
          first_name = supuser.get('first_name'),
          last_name = supuser.get('last_name'),
    )
    assert user_obj.is_superuser == True
    
    
@pytest.mark.django_db
def test_user_creation(client, django_user_model):
    user_obj = django_user_model.objects.create_user(
        username = normuser.get('username'),
        email = normuser.get('email'),
        password = normuser.get('password'),
        first_name = normuser.get('first_name'),
        last_name = normuser.get('last_name'),
    )
    assert user_obj.is_superuser == False