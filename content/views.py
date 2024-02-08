from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, './content/base.html')

def create (request):
	return render(request, './content/create.html')

def read(request):
	return render(request, './content/read.html')



