from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html", { "name":"Aaron"})

def about(request):
    return render(request, "about.html")