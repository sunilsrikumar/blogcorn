from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Hello there!</h1>")

def post_detail(request):
    return HttpResponse("<h1>Hello detail!</h1>")

def post_list(request):
    return HttpResponse("<h1>Hello list!</h1>")

def post_update(request):
    return HttpResponse("<h1>Hello update!</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello delete!</h1>")
