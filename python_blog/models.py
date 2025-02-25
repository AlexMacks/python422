from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode
# Функция get_user_model() возвращает модель пользователя, которая используется по умолчанию в проекте.
from django.contrib.auth import get_user_model


class Post(models.Model):

    # Определим статусы для поста. Проверено. Не проверено. Черновик. Опубликовано.
    STATUS_CHOICES = [
        ("draft", "Черновик"),
        ("review", "На проверке"),
        ("reviewed", "Проверено"),
        ("published", "Опубликовано"),
    ]


    title = models.CharField(max_length=100, unique=True, verbose_name="Заголовок")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг", blank=True, null=True)
    content = models.TextField(verbose_name="Контент")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name="Автор", related_name="posts", default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="review", verbose_name="Статус"
    )
    # категория - внешний ключ
    category = models.ForeignKey(
        "Category",  # Ссылка на модель Category
        on_delete=models.SET_NULL,  # При удалении категории, установить значение NULL
        blank=True,  # Не требуем в формах заполнения
        null=True,  # Разрешаем значение NULL в базе данных
        related_name="posts",  # Имя обратной связи
        default=None,  # По умолчанию значение NULL
        verbose_name="Категория",
    )
    tags = models.ManyToManyField("Tag", related_name="posts", verbose_name="Теги")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog:tag_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]
    



class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=250, unique=True, verbose_name="Слаг")
    description = models.TextField(
        blank=True, null=True, default="Без описания", verbose_name="Описание"
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("blog:category_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]