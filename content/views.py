from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.exceptions import ValidationError
from users.models import *

# Create your views here.

@login_required(login_url="/login/")
def home(request):
    context = {"blogs":articleCreateModel.objects.all()}
    return render(request, './content/base.html',context)

@login_required(login_url="/login/")
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

@login_required(login_url="/login/")
def readBlog(request,title):
    
    '''
    A function which is used to read a blog.
    '''
    if articleViewModel.objects.filter(btitle = title , username = request.user.username).count() < 1:
            articleViewModel.objects.create(
                btitle_id = articleCreateModel.objects.get(title=title),
                btitle = title,
                user_id = newUser.objects.get(username = request.user.username),
                username = request.user.username
            )
    read_blog_obj = {"blog":articleCreateModel.objects.filter(title=title).all()}
    comment_blog_obj = {"comment":articleViewModel.objects.filter(btitle = title , username = request.user.username).first().total_comments}
    blog_obj = {**read_blog_obj,**comment_blog_obj}
    return render(request, './content/read.html',context=blog_obj)


@login_required(login_url="/login/")
def updateBlog(request,title):
    
    '''
    A function which is used to update a blog.
    '''
    try:
        blog_obj = articleCreateModel.objects.filter(title=title).all()
        upd_obj = {"blog":blog_obj}
        if request.method == "POST":
            upd_obj_instance = articleCreateModel.objects.get(title=title)
            form = articleForm(request.POST, request.FILES , instance=upd_obj_instance)
            if form.is_valid():
                new_data = form.cleaned_data
                articleCreateModel.objects.filter(title=title).update(
                    title = new_data['title'],
                    catchline = new_data['catchline'],
                    script = new_data['script']
                )
                obj = articleCreateModel.objects.get(title=title)
                obj.thumbnail = new_data['thumbnail']
                obj.save()
                return redirect ("/blogs/")
            else:
                return render(request, './content/update.html',upd_obj)
        else:
            return render(request, './content/update.html',upd_obj) 
    except Exception as error:
        print(error)
        return redirect('/blogs/')

@login_required(login_url="/login/")
def deleteBlog(request,title):
    
    '''
        A function to delete the blog
    '''
    if articleCreateModel.objects.filter(title = title).count() == 1:
        del_blog_context = {"blog":title}
        if request.method == "POST":
            del_blog_title = request.POST['title']
            articleCreateModel.objects.filter(title = del_blog_title).all().delete()
            articleViewModel.objects.filter(btitle = del_blog_title).all().delete()
            return redirect("/blogs/")
        else:
            return render(request, "./content/delete.html",context=del_blog_context)
    else:
        return redirect("/blogs/")
            

@login_required(login_url="/login/")
def likeCommentBlog(request,title):
    blog_title = {"blog":title}
    raw_comments = articleViewModel.objects.get(btitle = title , username =request.user.username).per_comment
    if raw_comments is not None:
        raw_list_comments = list(raw_comments) # Breaking whole comments into piecewise chars and loading into list
        curated_comments = "".join(raw_list_comments).split("\n") # joining every piece of char in a string such that they form a list of such strings with no "\n"
        blog_comment = {"comment" : curated_comments}
        context = {**blog_title , **blog_comment}
    else:
        context = blog_title
    if request.method == "POST":
        form = likeCommentForm(request.POST)
        if form.is_valid():
            submitted_data = form.cleaned_data
            comment = submitted_data.get("per_comment")
            like = submitted_data.get("total_likes")
            obj = articleViewModel.objects.get(btitle = title , username = request.user.username)
            if comment is not None:
                if obj.per_comment is None:
                    obj.per_comment = comment
                else:
                    obj.per_comment = obj.per_comment + " \n " + comment 
                obj.total_comments  = obj.total_comments + 1
            
            if obj.total_likes == 0 and like: 
                obj.total_likes = 1
            obj.save()
            return redirect("/blogs/")
        else:
            return render(request,"./content/comment.html",context)
    else:
        return render(request,"./content/comment.html",context)
