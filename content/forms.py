from django.forms import ModelForm
from .models import articleCreateModel

class articleForm(ModelForm):
    class Meta:
        model = articleCreateModel
        fields = "__all__"