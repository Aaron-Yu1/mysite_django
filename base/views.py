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


def updatePost(request, pk):
    post = Post.objects.get(id = pk)
    context = { "post": post }
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.body = request.POST.get("description")
        post.save()
        return redirect("home")
    return render(request, "update_post.html", context)