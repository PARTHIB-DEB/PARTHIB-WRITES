from django.urls import path,include
from APP2 import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('content/',views.content,name="content"),
    path('create/',views.create,name="create"),
    path('read/<int:pk>/',views.read,name="read"),
    path('update/<int:pk>/',views.update,name="update"),
]