from django.shortcuts import render
from django.http import HttpResponse 
from django.urls import reverse
from .blog_data import dataset
from .models import Post, Category

# Create your views here.

def main(request):
    catalog_categories_url = reverse('blog:categories')
    catalog_tags_url = reverse('blog:tags')
    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_status": "moderator",
    }
    return render(request, "main.html", context)

def about(request):
    context = {
        "title": "О компании",
        "text": "Мы - команда профессионалов в области веб-разработки",
    }
    return render(request, "about.html", context)


def catalog_categories(request):
    CATEGORIES = Category.objects.all()

    context = {
        "title": "Категории",
        "text": "Текст страницы с категориями",
        "categories": CATEGORIES,
    }
    return render(request, "catalog_categories.html", context)

def category_detail(request, category_slug):

    category = Category.objects.filter(slug=category_slug).first()
    posts = Post.objects.filter(category=category)

    return render(
        request, "category_detail.html", {"category": category, "posts": posts}
    )

def catalog_tags(request):
    return HttpResponse("Каталог тегов")

def tag_detail(request, tag_slug):
    return HttpResponse(f"страница тега {tag_slug} ")

def catalog_posts(request):
        # Получаем все опубликованные посты
    posts = Post.objects.all()
    context = {"title": "Блог", "posts": posts}
    return render(request, "blog.html", context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {"title": post.title, "post": post}
    return render(request, "post_detail.html", context)


