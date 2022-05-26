from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    post = Post.objects.all()
    context = {'news': post, 'title': 'Список новин'}
    return render(request, 'news/index.html', context)
