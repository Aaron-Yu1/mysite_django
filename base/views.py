"""
This is define main function.
Author: Aaron
"""

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post,Comment

# Create your views here.


def search_posts(request):
    """This function for search posts"""
    post_search = ""
    if request.GET.get("search"):
        post_search = request.GET.get('search')
        posts = Post.objects.filter(
            Q(title__icontains = post_search) |
            Q(body__icontains = post_search)
        )
    else:
        posts = Post.objects.all()
    return posts

def index(request):
    """This function for index.html page."""
    posts = search_posts(request)
    context = { "posts": posts }
    return render(request, "index.html", context)


def about(request):
    """This function for about page"""
    return render(request, "about.html")

# auth
def loginUser(request):
    """This function for login user."""
    if request.user.is_authenticated:
        return redirect("home")
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context = {"message": "User name or password is not incorrect."}
    return render(request, "login.html", context)


@login_required(login_url="login")
def logoutUser(request):
    """This function for logout user."""
    logout(request)
    return redirect("home")

@login_required(login_url="login")
def myAccount(request):
    """This function for my account page."""
    user = request.user
    user_posts = Post.objects.filter(author=user)
    context = {"posts": user_posts}
    context["capitalize_username"] = request.user.username.capitalize()
    return render(request, "my_account.htm", context)

# post
def getPost(request, pk):
    """This function for view post page."""
    post = Post.objects.get(id = pk)
    if request.method == "POST":
        comment = request.POST.get("comment")
        Comment.objects.create(
            post = post,
            author = request.user,
            comment =comment
        )
    return render(request, "post_detail.html", { "post": post })

@login_required(login_url="login")
def deletePost(pk):
    """This function for delete post."""
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect("home")

@login_required(login_url="login")
def createPost(request):
    """This function for crete post."""
    context = {}
    if request.method == "POST":
        try:
            Post.objects.create(
                title = request.POST.get("title"),
                body = request.POST.get("description"),
                author = request.user
            )
            return redirect("home")
        except ImportError:
            context["message"] = "*Invalid details."
    return render(request, "new_post.html", context)

@login_required(login_url="login")
def updatePost(request, pk):
    """This function for update post"""
    post = Post.objects.get(id = pk)
    context = { "post": post }
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.body = request.POST.get("description")
        post.save()
        return redirect("home")
    return render(request, "update_post.html", context)
