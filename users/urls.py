from django.urls import path
from .views import *

urlpatterns = [
    path('',register,name="register"),
    path('login/',logUserIn,name="login"),
    path('logout/',logUserOut,name="logout"),
    path('drop-account/',destroy,name="delete"),
    path('profile/',profile,name="profile"),
    path('upd-profile/',updProfile,name="upd-profile"),
    path('upd-password/',passwordChange,name="upd-pass"),
]