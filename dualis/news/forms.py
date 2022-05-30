from turtle import title
from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=255)
    subtitle = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    #photo = forms.ImageField()
    body = forms.CharField()
    published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    

    '''subtitle = models.CharField(max_length=255, blank=True, verbose_name = 'Підзаголовок')
    slug = models.SlugField(max_length=255, unique=True, verbose_name = 'Слаг')
    body = models.TextField(blank=True, verbose_name = 'Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'Фото')
    meta_description = models.CharField(max_length=150, blank=True, verbose_name = 'Мета опис')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата створення')
    date_modified = models.DateTimeField(auto_now=True, verbose_name = 'Оновлено')
    publish_date = models.DateTimeField(blank=True, null=True, verbose_name = 'Дата публікування')
    published = models.BooleanField(default=False, verbose_name = 'Опубліковано')
    category''' 
