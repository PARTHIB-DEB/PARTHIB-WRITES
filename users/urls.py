from django.urls import path,include
from .views import *

urlpatterns = [
    path('',register,name="register")
]