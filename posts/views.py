from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Hello there!</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, id=3)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, "index.html", context)
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My user list"
    #     }
    # else:
    #     context = {
    #         "title": "list"
    #     }



def post_update(request):
    return HttpResponse("<h1>Hello update!</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello delete!</h1>")
