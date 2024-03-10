from django.forms import ModelForm 
from django import forms
from .models import *
from django import forms

class articleForm(ModelForm):
    class Meta:
        model = articleCreateModel
        fields = "__all__"

    
class likeForm(ModelForm):
    class Meta:
        model = articleViewModel
        fields = ("per_like",)
        
class CommentForm(ModelForm):
    class Meta:
        model = articleViewModel
        fields = ("per_comment",)