from django.shortcuts import render , redirect , HttpResponseRedirect
from users.forms import *
from django.contrib.auth import login ,authenticate , logout
from django.contrib.auth.decorators import login_required
from .models import newUser
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()

Sender_Email = os.getenv('EMAIL_HOST_USER')
Sender_Email_Password = os.getenv('EMAIL_HOST_PASSWORD')


# Create your views here.


# This set is used for caching by storing usernames locally (maybe will use later)
registered_users = list(newUser.new_objects.filter().values_list("username",flat=True))
# print(logged_users)
    

def register(request):
    
    '''
    This function is used to register or SignIn a new user into our webapp.
    Here all user inputs are being taken by the ModelForm UserForm and custom Model newUser
    Also, the defaultmanager 'new_objects' has been overrriden.
    '''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.clean_password2() # check if raw and confirm password are same or not
            user_datas = form.cleaned_data
            print(user_datas)
            username = user_datas['username']
            email = user_datas['email']
            
            if newUser.new_objects.filter(username = username).count()>0: # Checking if the username exists in Db
                raise ValidationError("USERNAME must be UNIQUE")
            
            if newUser.new_objects.filter(email = email).count()>0: # Checking if the email exists in Db
                raise ValidationError("EMAIL must be UNIQUE")
            
            if newUser.new_objects.filter(password = password).count()>0: # Checking if the password exists in Db
                raise ValidationError("PASSWORD must be UNIQUE")
            
            if username == Sender_Email:
                user_obj = newUser.new_objects.create_superuser(username=username,email=email,password=password)
                # user_obj.is_superuser = True
                # user_obj.is_user = True
                # user_obj.save()
            else:
                user_obj = newUser.new_objects.create_user(username=username,email=email,password=password)
            newUser.new_objects.filter(username=user_datas['username']).update(first_name=user_datas['first_name'] , last_name = user_datas['last_name'])
            login(request,user_obj)
            return redirect('/blogs/')
        else:
            print("\n\t\t OH NO!! FORM IS NOT VALID -> Register")
            return render(request, "./users/register.html")
    else:
        print("\n\t\t OH NO!! REQUEST IS NOT POST -> Register")
        return render(request, "./users/register.html")


def logUserIn(request):
    
    '''
    This function is used to log User in the app , if he/she is logged out but not signed out.
    '''
    if request.method == "POST":
        form = LoginForm(request.POST)
        user_datas = form.data
        username = user_datas['username']
        password = user_datas['password']
        user_obj = authenticate(request,username=username,password=password)
        if user_obj is not None:
            login(request,user_obj)
            return redirect('/blogs/')
        else:
            return redirect('/login/')
    else:
        return render(request, "./users/login.html")
    
        

@login_required(login_url="login/")
def logUserOut(request):
    uname = request.user.username
    logout(request)
    if newUser.new_objects.filter(username = uname).count()==1:
        return redirect ('/login/')


@login_required(login_url="login/")
def destroy(request):
    '''
    This function is used to Delete user's account.
    That means he/she wants to sign out.
    '''
    newUser.new_objects.filter(username = request.user.username).all().delete()
    return redirect('/')


@login_required(login_url="/login/")
def profile(request):
    context = {"blogs":newUser.new_objects.filter(username = request.user.username).all()}
    return render(request, './users/profile.html',context)