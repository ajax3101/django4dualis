from turtle import title
from unicodedata import category
from django.shortcuts import render, get_object_or_404
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
    #news_item = Post.objects.get(pk=news_id)
    news_item = get_object_or_404(Post, pk=news_id)
    context = {'news_item': news_item, }
    return render(request, 'news/view_news.html', context)