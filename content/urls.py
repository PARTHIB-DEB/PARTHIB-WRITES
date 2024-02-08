from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name="index"),
    path('create/',create,name="create"),
    path('read/',read,name="read"),
    path('user/',user,name="user"),
]