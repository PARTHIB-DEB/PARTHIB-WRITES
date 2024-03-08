from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.exceptions import ValidationError
from users.models import *

# Create your views here.

# print(articleCreateModel.objects.all())


@login_required(login_url="login")
def home(request):
    context = {"blogs":articleCreateModel.objects.all()}
    return render(request, './content/base.html',context)

@login_required(login_url="login")
def createBlog (request):
    '''
    A function which is used to create a new blog.
    '''
    if request.method == "POST":
        form = articleForm(request.POST , request.FILES)
        if form.is_valid():
            
            article_detail = form.cleaned_data
            title = article_detail['title']
            catchline = article_detail['catchline']
            thumbnail = article_detail['thumbnail']
            script = article_detail['script']
            
            blog = articleCreateModel.objects.create(title=title,catchline=catchline,thumbnail=thumbnail,script=script)
            blog.save()
            return redirect('/blogs/')
        else:
            return redirect('/blogs/')
    return render(request, './content/create.html')

@login_required(login_url="login")
def readBlog(request,title):
    
    '''
    A function which is used to read a blog.
    '''
    tcomments = articleViewModel.objects.values_list("per_comment",flat=True).count()
    tlikes = articleViewModel.objects.filter(per_like = 1).values_list("per_like",flat=True).count()
    read_blog = articleViewModel.objects.create(
        btitle = articleCreateModel.objects.get(title=title),
        total_likes = tlikes,
        total_comments = tcomments,
        username = newUser.objects.get(username = request.user.username)
    )
    read_blog.save()
    blog_obj = {"blog":articleCreateModel.objects.filter(title=title).all()}
    return render(request, './content/read.html',context=blog_obj)


@login_required(login_url="login")
def updateBlog(request,title):
    
    '''
    A function which is used to update a blog.
    '''
    try:
        blog_obj = articleCreateModel.objects.filter(title=title).all()
        upd_obj = {"blog":blog_obj}
        if request.method == "POST":
            upd_obj = articleCreateModel.objects.get(title=title)
            form = articleForm(request.POST, request.FILES , instance=upd_obj)
            if form.is_valid():
                new_data = form.cleaned_data
                print(new_data)
                articleCreateModel.objects.filter(title=title).update(
                    title = new_data['title'],
                    thumbnail = new_data['thumbnail'],
                    catchline = new_data['catchline'],
                    script = new_data['script']
                )
                return redirect ("/blogs/")
            else:
                return redirect(f'/blogs/update-blog/{title}')
        else:
            return render(request, './content/update.html',upd_obj) 
    except Exception as error:
        print(error)
        return redirect('/blogs/')

@login_required(login_url="login")
def deleteBlog(request,pk):
    
    '''
        A function to delete the blog
    '''
    if request.method == "POST":
        form = DeleteArticleForm(request.POST)
        if form.is_valid():
            user_datas = form.cleaned_data
            response = list(user_datas['question']) # To check if user's response is the expected one or not
            if ((response[0]=="Y" or response[0]=="y") and (response[1]=="e" or response[1]=="E") and (response[2]=="S" or response[2]=="s") and len(response)==3):
                del_obj = articleCreateModel.objects.filter(title = pk)
                del_obj.delete()
                return render(request,'./content/base.html')
        return render(request,'./content/base.html')
    return render(request,'./content/base.html')


@login_required(login_url="login")
def per_like_comment_fn(request,pk):
    form = LikeCommentForm()
    if request.method == "POST":
        form = LikeCommentForm(request.POST)
        if form.is_valid():
            raw_response = form.cleaned_data
            curate_comment = ""
            raw_like ,  raw_comment = raw_response[0] , raw_response[1]
            list_comment = list(raw_comment)
            for i in range(len(list_comment)):
                if list_comment[i] != " ":
                    curate_comment += list_comment[i]
            articleCreateModel.objects.filter(title = pk).update(per_like = raw_like, per_comment = curate_comment)
            return render(request,'./content/base.html')
        return render(request,'./content/base.html')
    return render(request,'./content/comment.html',{"form":form})
