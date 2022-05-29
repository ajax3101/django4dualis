from turtle import title
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Category


def index(request):
    post = Post.objects.all()
    
    context = {'news': post, 'title': 'Список новин', }
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    post = Post.objects.filter(category_id=category_id)
    
    category = Category.objects.get(pk=category_id)
    context = {'news': post, 'category': category, }
    return render(request, 'news/category.html', context)

def view_news(request, news_id):
    news_item = Post.objects.all()