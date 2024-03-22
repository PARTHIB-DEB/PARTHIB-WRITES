from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
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


def register(request):
    
    '''
    This function is used to register or SignIn a new user into our webapp.
    Here all user inputs are being taken by the ModelForm UserForm and custom Model newUser
    Also, the defaultmanager 'objects' has been overrriden.
    '''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.clean_password2() # check if raw and confirm password are same or not
            user_datas = form.cleaned_data
            print(user_datas)
            username = user_datas['username']
            email = user_datas['email']
            
            if newUser.objects.filter(username = username).count()>0: # Checking if the username exists in Db
                raise ValidationError("USERNAME must be UNIQUE")
            
            if newUser.objects.filter(email = email).count()>0: # Checking if the email exists in Db
                raise ValidationError("EMAIL must be UNIQUE")
            
            if newUser.objects.filter(password = password).count()>0: # Checking if the password exists in Db
                raise ValidationError("PASSWORD must be UNIQUE")
            
            if username == Sender_Email:
                newUser.objects.create_superuser(username=username,email=email,password=password)
                # is_staff = True
                # is_superuser = True
                # newUser.objects.filter(username = request.user.username).save_superattrs(
                #     is_staff,is_superuser
                # )
            else:
                user_obj = newUser.objects.create_user(username=username,email=email,password=password)
            newUser.objects.filter(username=user_datas['username']).update(first_name=user_datas['first_name'] , last_name = user_datas['last_name'])
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
    if newUser.objects.filter(username = uname).count()==1:
        return redirect ('/login/')


@login_required(login_url="login/")
def destroy(request):
    '''
    This function is used to Delete user's account.
    That means he/she wants to sign out.
    '''
    newUser.objects.filter(username = request.user.username).all().delete()
    return redirect('/')


@login_required(login_url="/login/")
def profile(request):
    context = {"blogs":newUser.objects.filter(username = request.user.username).all()}
    return render(request, './users/profile.html',context)


@login_required(login_url="/login/")
def updProfile(request):
    if request.method == "GET":
        return render(request, './users/upd_profile.html')
    else:
        form = UserForm(request.POST or None)
        data = form.data
        x =  newUser.objects.filter(username = request.user.username).update(
            username = data['username'],
            email = data['email'],
            first_name = data['first_name'],
            last_name = data['last_name']
        )
        x
        return redirect('/blogs/')


@login_required(login_url='/login/')
def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/blogs/')
    else:
        form = PasswordChangeForm(user=request.user)        
        return render(request,'./users/upd_password.html',context={"form":form})
        
        

        