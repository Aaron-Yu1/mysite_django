from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about),
    path("post/<str:pk>", views.getPost, name="post_detail"),
    path("post/<str:pk>/delete", views.deletePost, name="post_delete"),
]