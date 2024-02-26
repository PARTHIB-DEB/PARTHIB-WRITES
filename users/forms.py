from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, ValidationError
from .models import newUser
from django import forms

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = newUser
        fields = UserCreationForm.Meta.fields + ("email",)
    
    def clean_password2(self) -> str:
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginForm(ModelForm):
    class Meta:
        model = newUser
        fields = ("username","password")
        
        
class DeleteForm(ModelForm):
    question = forms.CharField()
    class Meta:
        model = newUser
        fields = ("username","password","question")
