from datetime import datetime
from django.shortcuts import render

from .models import Post

def home(request):
    post_list = Post.objects.all()

    return render(request, "index.html", {'post_list': post_list})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, "post.html", {'post': post})

def hello(request):
    return render(request, "hello_world.html", {'current_time': str(datetime.now())})
