from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.exceptions import ValidationError
from users.models import *

# Create your views here.

@login_required(login_url="login/")
def home(request):
	return render(request, './content/base.html')

@login_required(login_url="login/")
def createBlog (request):
    '''
    A function which is used to create a new blog.
    '''
    if request.method == "POST":
        form = articleForm(request.POST,request.FILES)
        if form.is_valid():
            
            article_detail = form.cleaned_data
            title = article_detail['title']
            catchline = article_detail['catchline']
            thumbnail = article_detail['thumbnail']
            script = article_detail['script']
            
            blog = articleCreateModel.objects.create(title=title,catchline=catchline,thumbnail=thumbnail,script=script)
            blog.save(force_insert=True)
            return render(request, './content/base.html')
        else:
            return render(request, './content/create.html')
    return render(request, './content/create.html')

@login_required(login_url="login/")
def readBlog(request,uname,pk):
    
    '''
    A function which is used to create a new blog.
    '''
    
    read_blog = articleViewModel.objects.create(
		btitle = articleCreateModel.objects.filter(title=pk).title,
		username = newUser.objects.filter(username=uname).username
	)
    read_blog.save(force_insert=True)
    blog_obj = {"blog":articleCreateModel.objects.get(title=pk)}
    return render(request, './content/read.html',blog_obj)

@login_required(login_url="login/")
def updateBlog(request,pk):
    
    '''
    A function which is used to create a new blog.
    '''
    blog_obj = articleCreateModel.objects.get(title=pk)
    upd_obj = {"blog":blog_obj}
    if request.method == "POST":
        form = articleForm(request.POST,request.FILES)
        if form.is_valid():
            article_detail = form.cleaned_data
            
            if (article_detail['title'] != blog_obj.title) and (articleCreateModel.objects.filter(title=article_detail['title']).count() == 0):
                title = article_detail['title']
                articleCreateModel.objects.filter(title=blog_obj.title).update(title=title)
            
            if (article_detail['catchline'] != blog_obj.catchline) and (articleCreateModel.objects.filter(catchline=article_detail['catchline']).count() == 0):
                catchline = article_detail['catchline']
                articleCreateModel.objects.filter(catchline=blog_obj.catchline).update(catchline=catchline)
            
            if (article_detail['thumbnail'] != blog_obj.thumbnail) :
                thumbnail = article_detail['thumbnail']
                articleCreateModel.objects.filter(title=article_detail['title']).update(thumbnail=thumbnail)
                
            if (article_detail['script'] != blog_obj.script) and (articleCreateModel.objects.filter(script=article_detail['script']).count() == 0):
                script = article_detail['script']
                articleCreateModel.objects.filter(script=blog_obj.script).update(script=script)

            return render(request, './content/base.html')
        else:
            return render(request, './content/create.html')
    return render(request, './content/read.html',upd_obj) # Change this template

@login_required(login_url="login/")
def deleteBlog(request):
    pass



