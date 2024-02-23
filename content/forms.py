from django.forms import ModelForm , forms
from .models import *

class articleForm(ModelForm):
    class Meta:
        model = articleCreateModel
        fields = "__all__"

class DeleteArticleForm(forms):
    question = forms.forms.CharField(max_length=True)
    
class LikeCommentForm(ModelForm):
    class Meta:
        model = articleViewModel
        fields = ("per_like","per_comment")