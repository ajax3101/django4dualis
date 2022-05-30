from turtle import title
from django import forms
from .models import Category, Profile

class NewsForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={"class":"form-control"}))
    subtitle = forms.CharField(max_length=255, label='Підзаголовок', required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    #slug = forms.SlugField(max_length=255, label='Слаг', required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    #photo = forms.ImageField()
    body = forms.CharField(label='Контент', required=False, widget=forms.Textarea(attrs={"class":"form-control", "rows":"5"}))
    published = forms.BooleanField(label='Опубліковано', initial=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категорія', empty_label='Оберіть категорію', widget=forms.Select(attrs={"class":"form-control"}))
    author = forms.ModelChoiceField(queryset=Profile.objects.all(), label='Автор', empty_label='Оберіть Автора', widget=forms.Select(attrs={"class":"form-control"}))
 