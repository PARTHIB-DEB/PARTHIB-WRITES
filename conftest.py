import pytest
from django.urls import reverse
from pytest_django.fixtures import django_user_model
from users.models import *
from users.forms import UserForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from dotenv import load_dotenv
import os

load_dotenv()

Sender_Email = os.getenv("EMAIL_HOST_USER")
Sender_Email_Password = os.getenv("EMAIL_HOST_PASSWORD")
usermodel = django_user_model



class ConfUserModel:


    def __init__(self, **data) -> None:
        form = UserForm(data=data)
        if form.is_valid():
            user_data = form.cleaned_data
            self.username = (user_data.get("username"),)
            self.email = (user_data.get("email"),)
            self.password = (user_data.get("password"),)
            self.first_name = (user_data.get("first_name"),)
            self.last_name = (user_data.get("last_name"),)
            self.is_logged_in = 0


    def create_a_user(self):
        if self.email == Sender_Email:
            user_obj = usermodel.objects.create_superuser(
                username=self.username,
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name,
            )
            assert user_obj.is_superuser == True
            return user_obj.username
        else:
            user_obj = usermodel.objects.create_user(
                username=self.username,
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name,
            )
            assert user_obj.is_superuser == True
            return user_obj.username

    def update_a_user(self, data, create_a_user: str):
        prev_user_obj = usermodel.objects.filter(username=create_a_user).all()
        form = UserForm(data=data, instance=prev_user_obj)
        if form.is_valid():
            new_data = form.cleaned_data
            assert new_data not in prev_user_obj == True
            form.save()

    def update_a_user_password(self, data, create_a_user: str):
        prev_user_obj = usermodel.objects.filter(username=create_a_user).all()
        form = PasswordChangeForm(data=data, instance=prev_user_obj)
        if form.is_valid():
            new_password = form.clean_new_password2()
            assert new_password != prev_user_obj.password
            form.save()

    def login_a_user(self, data):
        form = LoginForm(data=data)
        user_data = form.data
        user_obj = authenticate(
            username=user_data["username"], password=user_data["password"]
        )
        if user_obj is not None:
            self.is_logged_in = 1
        assert self.is_logged_in == 1
