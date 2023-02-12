from django.forms import ModelForm
from .models import *

class Blogform(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'catch','image','details']