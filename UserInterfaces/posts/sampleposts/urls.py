from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("getUsers", views.GetUsers, name="getusers"),
    path("posts", views.posts, name="posts")    
]