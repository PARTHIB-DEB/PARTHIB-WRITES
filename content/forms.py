from django.forms import ModelForm 
from .models import *

class articleForm(ModelForm):
    class Meta:
        model = articleCreateModel
        fields = "__all__"

        
class likeCommentForm(ModelForm):
    class Meta:
        model = articleViewModel
        fields = ("total_likes","per_comment",)