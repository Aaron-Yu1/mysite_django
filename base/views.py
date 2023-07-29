from django.shortcuts import render,redirect
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", { "posts": posts})

def about(request):
    return render(request, "about.html")

def getPost(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, "post_detail.html", { "post": post })

def deletePost(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect("home")