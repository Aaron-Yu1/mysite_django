from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post

# Create your views here.


def search_posts(request):
    post_search = ""
    if request.GET.get("search"):
        post_search = request.GET.get('search')
        posts = Post.objects.filter(Q(title__icontains = post_search) | Q(body__icontains = post_search))
    else:
        posts = Post.objects.all()
    return posts

def index(request):
    posts = search_posts(request)
    context = { "posts": posts }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")

# auth
def loginUser(request):
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
    logout(request)
    return redirect("home")

@login_required(login_url="login")
def myAccount(request):
    user = request.user
    user_posts = Post.objects.filter(author=user)
    context = {"posts": user_posts}
    context["capitalize_username"] = request.user.username.capitalize()
    return render(request, "my_account.htm", context)

# post 
def getPost(request, pk):
    post = Post.objects.get(id = pk)
    return render(request, "post_detail.html", { "post": post })

@login_required(login_url="login")
def deletePost(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    return redirect("home")

@login_required(login_url="login")
def createPost(request):
    context = {}
    if request.method == "POST":
        try:
            Post.objects.create(
                title = request.POST.get("title"),
                body = request.POST.get("description"),
                author = request.user
            )
            return redirect("home")
        except:
            context["message"] = "*Invalid details."
    return render(request, "new_post.html", context)

@login_required(login_url="login")
def updatePost(request, pk):
    post = Post.objects.get(id = pk)
    context = { "post": post }
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.body = request.POST.get("description")
        post.save()
        return redirect("home")
    return render(request, "update_post.html", context)