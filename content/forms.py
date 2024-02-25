from django.forms import ModelForm 
from django import forms
from .models import *
from django import forms

class articleForm(ModelForm):
    class Meta:
        model = articleCreateModel
        fields = "__all__"

class DeleteArticleForm(forms.Form):
    question = forms.CharField(label="question",max_length=3)
    
class LikeCommentForm(ModelForm):
    class Meta:
        model = articleViewModel
        fields = ("per_like","per_comment")