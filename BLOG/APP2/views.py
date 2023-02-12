from django.shortcuts import render, HttpResponseRedirect, redirect,HttpResponse
from APP2.models import Blog
from APP2.forms import Blogform


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def create(request):
    if request.method == "POST":
        # form = Blogform(request.POST)
        # if form.is_valid():
        #     title = form.cleaned_data['title']
        #     catch = form.cleaned_data['catch']
        #     image = form.cleaned_data['image']
        #     details = form.cleaned_data['details']
        # else:
        #     form = Blogform()

        title = request.POST['title']
        catch = request.POST['catch']
        image = request.FILES['image']
        slug=request.POST['slug']
        details = request.POST['details']
        blog = Blog.objects.create(
            title=title, catch=catch, image=image,slug=slug, details=details)
        blog.save
        return render(request,'create.html')
    else:
        return render(request, 'create.html')

def content(request):
    context = {"myblog": Blog.objects.all()}
    return render(request, 'content.html', context)

def read(request,pk):
    context = {"object": Blog.objects.filter(slug=pk).all()}
    return render(request, 'read.html', context)
        
def update(request,pk):
    blog_obj=Blog.objects.filter(slug=pk).all()
    initial={'myblog':blog_obj}
    # form=Blogform(initial=initial)
    if request.method == "POST":
        form = Blogform(request.POST)
        # if form.is_valid():
        #     title = form.cleaned_data['title']
        #     catch = form.cleaned_data['catch']
        #     details = form.cleaned_data['details']
        # else:
        #     form = Blogform()
        title = request.POST['title']
        catch = request.POST['catch']
        details = request.POST['details']
        Blog.objects.filter(slug=pk).update(
            title=title, catch=catch, details=details)
        return redirect('/')
    return render(request, 'update.html',initial)

