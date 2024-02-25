from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('create-blog/',createBlog,name="create"),
    # path('read-blog/<str:username>/<str:pk>/',readBlog,name="read"),
    path('read-blog/',readBlog,name="read"),
    path('update-blog/<str:pk>/',updateBlog,name="update"),
    path('delete-blog/<str:pk>/',deleteBlog,name="delete"),
]