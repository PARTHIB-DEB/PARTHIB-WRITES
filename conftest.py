import pytest
from django.urls import reverse
from users.models import *
from users.forms import UserForm, LoginForm
from content.models import *
from content.forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from dotenv import load_dotenv
import os

load_dotenv()

Sender_Email = os.getenv("EMAIL_HOST_USER")
Sender_Email_Password = os.getenv("EMAIL_HOST_PASSWORD")



class ConfUserModel:
    
    django_user_model = newUser
    
    @pytest.fixture(scope='class')
    def take_data(self,**data):
        form = UserForm(data=data)
        if form.is_valid():
            return data
        
    @pytest.fixture(scope='function')
    def create_a_user(self,**old_data):
            if old_data.get("email") == Sender_Email:
                user_obj = self.django_user_model.objects.create_superuser(
                    username=old_data.get("username"),
                    email=old_data.get("email"),
                    password=old_data.get("password"),
                    first_name=old_data.get("first_name"),
                    last_name=old_data.get("last_name"),
                )
                assert user_obj.is_superuser == True
                return throw_name(old_data.get("username"))
            else:
                user_obj = self.django_user_model.objects.create_user(
                    username=old_data.get("username"),
                    email=old_data.get("email"),
                    password=old_data.get("password"),
                    first_name=old_data.get("first_name"),
                    last_name=old_data.get("last_name"),
                )
                assert user_obj.is_superuser == False
                return old_data.get("username")

    def update_a_user(self, data:dict , **old_data):
        form = UserForm(data=data)
        if form.is_valid():
            clean_data = form.clean()
            self.django_user_model.objects.filter(username = old_data.get("username")).update(
                username = clean_data.get("username"),
                email = clean_data.get("email"),
                password = clean_data.get("password"),
                first_name = clean_data.get("first_name"),
                last_name = clean_data.get("last_name")
            )
            assert old_data != data

    def update_a_user_password(self, data, **old_data):
        user_obj = self.django_user_model.objects.filter(username=old_data.get('username')).all()
        form = PasswordChangeForm(data=data, user=old_data.get('username'))
        if form.is_valid():
            new_password = form.clean_new_password2()
            form.save()
            assert new_password != user_obj.password

    def login_a_user(self, data , **old_data):
        form = LoginForm(data=data)
        user_data = form.data
        user_obj = authenticate(
            username=user_data["username"], password=user_data["password"]
        )
        if user_obj:
            form.save()
            assert True


class ConfBlogModel :
    
    blog = articleCreateModel
    view_blog = articleViewModel
    viewer = newUser
    
    @pytest.fixture(scope='class')
    def take_data(self,**data):
        form = UserForm(data=data)
        if form.is_valid():
            return data
        
    
    def create_a_blog(self,**old_data):
        blog = self.blog.objects.create(**old_data)
        blog.save()
        assert self.blog.objects.all().count() > 0
    
    def update_a_blog(self , data:dict , **old_data):
        form = articleForm(data=data)
        if form.is_valid():
            clean_data = form.clean()
            blog_obj = self.blog.objects.get(title = old_data.get("title"))
            if clean_data.get("title") != blog_obj.title:
                blog_obj.title = clean_data.get("title")
            if clean_data.get("catchline") != blog_obj.catchline:
                blog_obj.catchline = clean_data.get("catchline")
            if clean_data.get("script") != blog_obj.script:
                blog_obj.script = clean_data.get("script")
            blog_obj.save()
            assert old_data != data
    
    # def retrieve_a_blog(self ,**old_data):
    #     try:
    #         uname = self.viewer.objects.get(email = Sender_Email).username
    #         x = self.view_blog.objects.update_or_create(
    #             btitle_id = self.blog.objects.get(title=old_data.get("title")),
    #             btitle = self.blog.objects.get(title=old_data.get("title")).title,
    #             user_id = self.viewer.objects.filter(username = uname).first(),
    #             username = uname
    #         )
    #         x.save()
    #         assert self.view_blog.objects.all().count() > 0
            
    #     except Exception as error:
    #         print(error)
        
        
