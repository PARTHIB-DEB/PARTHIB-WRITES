from django.shortcuts import render
from users.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login ,authenticate , logout
from django.contrib.auth.decorators import login_required 

# Create your views here.

# filtered_usernames =  User.objects.filter(is_superuser=False , is_staff=False).values_list("username",flat=True)
# logged_in_user = set(filtered_usernames)
# print(logged_in_user)

def register(request):
    # form = UserForm()
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         user_datas = form.cleaned_data
    #         user_obj = User.objects.create_user(username=user_datas.pop('username'),password=user_datas.pop('password1'))
    #         user_obj.first_name = request.POST['first_name']
    #         user_obj.last_name = request.POST['last_name']
    #         user_obj.save()
    #         logged_in_user.add(user_obj.username)
    #         login(request,user_obj)
    #         return render(request,'./content/base.html')
    #     else:
    #         return render(request,'./users/register.html')
    # return render(request,'./users/register.html')
    pass

def logUserIn(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     piece_user = authenticate(request,username=username,password=password)
    #     if piece_user is not None:
    #         if username not in logged_in_user:
    #             logged_in_user.add(username)
    #         login(request,piece_user)
    #         return render(request,'./content/base.html')
    #     else:
    #         return render(request,'./users/register.html')
    # return render(request,'./users/register.html')
    pass

# @login_required(login_url="")
def logUserOut(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     if username in logged_in_user:
    #         logged_in_user.remove(username)
    #     logout(request)
    # return render(request,'./users/register.html')
    pass

# @login_required(login_url="")
def destroy(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     username = request.POST['password']
    #     question = request.POST['ques']
    #     if question == "Y" or question == "y":
    #         logged_in_user.remove(username)
    #         del_user = User.objects.get(username=username)
    #         del_user.delete()
    #     else:
    #         return render(request,'./users/register.html')
    # return render(request,'./users/register.html')
    pass
        