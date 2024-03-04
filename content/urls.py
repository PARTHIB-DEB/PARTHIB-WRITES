from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('create-blog/',createBlog,name="create"),
    path('read-blog/<str:username>/<str:title>/',readBlog,name="read"),
    path('update-blog/<str:pk>/',updateBlog,name="update"),
    path('delete-blog/<str:pk>/',deleteBlog,name="delete"),
    path('profile/',profile,name="profile"),
]