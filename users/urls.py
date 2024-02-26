from django.urls import path
from .views import *

urlpatterns = [
    path('',register,name="register"),
    path('login',logUserIn,name="login"),
    path('logout',logUserOut,name="logout"),
    path('drop-account',destroy,name="delete"),
]