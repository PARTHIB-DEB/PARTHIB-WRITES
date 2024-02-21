from django.contrib.auth.forms import UserCreationForm
from .models import newUser


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = newUser
        fields = UserCreationForm.Meta.fields + ("email",)