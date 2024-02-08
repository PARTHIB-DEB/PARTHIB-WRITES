from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'base.html')

def create (request):
	return render(request, 'create.html')

def read(request):
	return render(request, 'read.html')

def user(request):
	return render(request, 'user.html')



