from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import *
from users.forms import UserForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    model = newUser
    
admin.site.register(newUser,CustomUserAdmin)