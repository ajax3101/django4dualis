from django.conf import settings
from django.db import models

# Create your models here.
'''Создаем модели данных для новостей

Создадим три следующие модели данных:

Profile - хранит информацию о пользователях новости.
Tag  - содержит данные о категориях, по которым группируются записи новости.
Post  - используется для хранения контента и метаданных о каждом посте новости.
############################################################################

Модель Profile
Модель профиля содержит несколько полей:

user — связь с пользователем Django (связь один-к-одному).
website — опциональный URL, по которому можно узнать больше о пользователе.
bio — опциональное небольшое био («о себе»).
'''

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)
# Метод __str__ сделает удобнее отображение профилей в панели администратора .
    def __str__(self):
        return self.user.get_username()

# Модель Tag
# В модели Tag будет единственное поле, короткое имя тега

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Модель Post
# Модель Post — самая сложная, содержит множество полей: заголовок (title), подзаголовок (subtitle),
# слаг (slug, уникальная часть URL для нашего поста), контент поста (body) и т.д.

class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)


'''
Пояснения:
В подклассе Meta мы указываем порядок сортировки постов (ordering) по дате публикации.
Аргумент on_delete = models.PROTECT для поля author гарантирует, что при удалении постов мы случайно не удалим автора.
Каждый тег может быть связан со многими сообщениями, поэтому для поля tags используется отношение ManyToManyField.
'''
