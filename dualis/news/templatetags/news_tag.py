from atexit import register
from django import template
from news.models import Category


register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='World', arg2='Hello'):
    categories = Category.objects.all()
    return {"categories": categories, }