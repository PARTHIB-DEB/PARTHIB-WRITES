from django.shortcuts import render
from users.forms import *
from django.contrib.auth import login ,authenticate , logout
from django.contrib.auth.decorators import login_required
from .models import newUser
from django.core.exceptions import ValidationError

# Create your views here.


# This set is used for caching by storing usernames locally (maybe will use later)
# filtered_usernames =  newUser.objects.filter(is_superuser=False , is_staff=False).values_list("username",flat=True)
# registered_users = set(filtered_usernames)


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
            
            if newUser.objects.filter(usename = username).count()>0: # Checking if the username exists in Db
                raise ValidationError("USERNAME must be UNIQUE")
            
            if newUser.objects.filter(email = email).count()>0: # Checking if the email exists in Db
                raise ValidationError("EMAIL must be UNIQUE")
            
            if newUser.objects.filter(password = password).count()>0: # Checking if the password exists in Db
                raise ValidationError("PASSWORD must be UNIQUE")
            
            user_obj = newUser.objects.create_user(username=username,email=email,password=password)
            user_obj.first_name = user_datas['username']
            user_obj.last_name = user_datas['last_name']
            # registered_users.add(user_obj.username)
            
            login(request,user_obj) # for absolutely new users , logging them in automatically
            return render(request,'./content/base.html')
        
        return render(request,'./users/register.html')
        
    return render(request,'./users/register.html')
    
@login_required(login_url="/")
def logUserIn(request):
    
    '''
    This function is used to log User in the app , if he/she is logged out but not signed out.
    '''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_datas = form.cleaned_data
            username = user_datas['username']
            password = user_datas['password']
            
            user_obj = authenticate(username=username,password=password) 
            if user_obj is not None:
                login(request,user_obj)
            else:
                raise ValidationError("USER IS ANONYMOUS")
            
        return render(request,'./users/login.html')
    
    return render(request,'./users/login.html')
        

@login_required(login_url="/login/")
def logUserOut(request):
    logout(request)
    return render(request,'./content/base.html')


@login_required(login_url="/login/")
def destroy(request):
    '''
    This function is used to Delete user's account.
    That means he/she wants to sign out.
    '''
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            user_datas = form.cleaned_data
            response = list(user_datas['question']) # To check if user's response is the expected one or not
            if ((response[0]=="Y" or response[0]=="y") and (response[1]=="e" or response[1]=="E") and (response[2]=="S" or response[2]=="s") and len(response)==3):
                del_obj = newUser.objects.filter(usename=user_datas['username'] , password=user_datas['password'])
                # registered_users.remove(user_datas['username'])
                del_obj.delete()
                return render(request,'./users/register.html')
            
            return render(request,'./content/base.html')
        
        return render(request,'./content/base.html')
    
    return render(request,'./content/base.html')
        