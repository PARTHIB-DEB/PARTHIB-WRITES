from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash , get_user_model
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
            username = user_datas['username']
            email = user_datas['email']
            
            if newUser.objects.filter(username = username).count()>0: # Checking if the username exists in Db
                raise ValidationError("USERNAME must be UNIQUE")
            
            if newUser.objects.filter(email = email).count()>0: # Checking if the email exists in Db
                raise ValidationError("EMAIL must be UNIQUE")
            
            if newUser.objects.filter(password = password).count()>0: # Checking if the password exists in Db
                raise ValidationError("PASSWORD must be UNIQUE")
            
            if email == Sender_Email:
                user_obj = newUser.objects.create_superuser(username=username,email=email,password=password , first_name=user_datas['first_name'] , last_name = user_datas['last_name'])
            else:
                user_obj = newUser.objects.create_user(username=username,email=email,password=password , first_name=user_datas['first_name'] , last_name = user_datas['last_name'])
            subject = "Parthib-writes | Account Confirmation from Parthib-writes"
            message = f"Hey {username}, If you got this mail , that means your account have been verified and created.\n You are now an authorised user so jump into http://127.0.0.1:8000/blogs/"
            from_mail = Sender_Email
            to_email = [email,]
            send_mail(subject=subject,message=message,from_email=from_mail,recipient_list=to_email,fail_silently=True)
            login(request,user_obj)
            return redirect('/blogs/')
        else:
            return render(request, "./users/register.html")
    else:
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
        user_obj = authenticate(username=username,password=password)
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
    if request.method == "POST":
        uobj = newUser.objects.get(username = request.user.username)
        form = updateUserForm(request.POST or None , instance=uobj)
        if form.is_valid():
            new_data = form.cleaned_data
            
            if uobj.username != new_data.get("username"):
                uobj.username = new_data.get("username")
                
            if uobj.email != new_data.get("email"):
                uobj.email = new_data.get("email")
                
            if uobj.first_name != new_data.get("first_name"):
                uobj.first_name = new_data.get("first_name")
                
            if uobj.last_name != new_data.get("last_name"):
                uobj.last_name = new_data.get("last_name")
            
            uobj.save()
            return redirect('/blogs/')
        else:
           return render(request, './users/upd_profile.html') 
    else:
        return render(request, './users/upd_profile.html')


@login_required(login_url='/login/')
def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/blogs/')
    form = PasswordChangeForm(user=request.user)        
    return render(request,'./users/upd_password.html',context={"form":form})
        
        
        