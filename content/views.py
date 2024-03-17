from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.exceptions import ValidationError
from users.models import *

# Create your views here.

# print(articleCreateModel.objects.all())


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
    if request.method == "POST":
        form = likeForm(request.POST)
        if form.is_valid():
            articleCreateModel.objects.filter(btitle=title).update(per_like = 1)
    else:
        tcomments = articleViewModel.objects.filter(username=request.user.username).values_list("per_comment",flat=True).count()
        tlikes = articleViewModel.objects.filter(per_like = 1).values_list("per_like",flat=True).count()
        if articleViewModel.objects.filter(btitle = title , username = request.user.username).count()==1:
            articleViewModel.objects.filter(btitle = title , username = request.user.username).update(
                btitle_id = articleCreateModel.objects.get(title=title),
                btitle = articleCreateModel.objects.get(title=title).title,
                total_likes = tlikes,
                total_comments = tcomments,
                # user_id = newUser.objects.get(username = request.user.username),
                # username = newUser.objects.get(username = request.user.username).username
            )
        else:
            articleViewModel.objects.create(
                btitle_id = articleCreateModel.objects.get(title=title),
                btitle = articleCreateModel.objects.get(title=title).title,
                total_likes = tlikes,
                total_comments = tcomments,
                user_id = newUser.objects.get(username = request.user.username),
                username = newUser.objects.get(username = request.user.username).username
            )
        blog_obj = {"blog":articleCreateModel.objects.filter(title=title).all()}
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
                # print(new_data)
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
def CommentBlog(request,title):
    context = {"blog":title}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['per_comment']
            obj = articleViewModel.objects.get(btitle = title , username = request.user.username)
            if obj.per_comment is None:
                obj.per_comment = comment
            else:
                obj.per_comment = str(obj.per_comment)+"\n"+str(comment)
            obj.total_comments = obj.total_comments + 1
            obj.save()
            return redirect("/blogs/")
        else:
            return render(request,"./content/comment.html",context)
    else:
        return render(request,"./content/comment.html",context)

