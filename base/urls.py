"""
This is define the urls of site.
Author: Aaron
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about),
    path("post/<str:pk>", views.getPost, name="post_detail"),
    path("post/<str:pk>/delete", views.deletePost, name="post_delete"),
    path("post_create/", views.createPost, name="post_create"),
    path("post/<str:pk>/edit", views.updatePost, name="update_post"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("my_account/", views.myAccount, name="my_account"),
]
