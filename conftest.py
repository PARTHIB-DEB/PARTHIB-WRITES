import pytest

from django.urls import reverse
from users.models import *
from users.forms import *
from dotenv import load_dotenv
import os

load_dotenv()

Sender_Email = os.getenv('EMAIL_HOST_USER')
Sender_Email_Password = os.getenv('EMAIL_HOST_PASSWORD')


# Testing will be done for these functions
# Signin (register)  , Signout (Delete) , Login , Logout , Likes and Comments (Probably)
# Probably a Class will be best for this case

@pytest.mark.django_db
class TestUserModel:
  def __init__(self , **data) -> None:
    form = UserCreationForm(data)
    user_data = form.cleaned_data
    self.username = user_data.get("username"),
    self.email = user_data.get("email"),
    self.password = user_data.get("password"),
    self.first_name = user_data.get("first_name"),
    self.last_name = user_data.get("last_name")
    
  @pytest.fixture()
  def create_a_user(self,django_user_model):
      if self.email == Sender_Email:
            user_obj = django_user_model.objects.create_superuser(
                username = self.username,
                email = self.email,
                password = self.password,
                first_name = self.first_name,
                last_name = self.last_name,
            )
            assert user_obj.is_superuser == True
            return user_obj['username']
      else:
            user_obj = django_user_model.objects.create_superuser(
                username = self.username,
                email = self.email,
                password = self.password,
                first_name = self.first_name,
                last_name = self.last_name,
            )
            assert user_obj.is_superuser == True
            return user_obj['username']
        
  def update_a_user(self,django_user_model,create_a_user : str,**details):
      user_obj = django_user_model.objects.filter(username = create_a_user).update(**details)
      return user_obj
  
  def update_a_user_password(self,django_user_model, data , create_a_user : str):
      pass
  
    
      