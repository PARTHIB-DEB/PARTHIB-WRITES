from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('create-blog/',createBlog,name="create"),
    path('read-blog/<str:title>/',readBlog,name="read"),
    path('update-blog/<str:title>/',updateBlog,name="update"),
    path('delete-blog/<str:title>/',deleteBlog,name="delete"),
    path('comment-blog/<str:title>/',likeCommentBlog,name="comment")
]