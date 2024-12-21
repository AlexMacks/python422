# APP URLS
from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_categories, catalog_tags, catalog_posts, category_detail, tag_detail, post_detail

urlpatterns = [
    # Категории
    path('categories/', catalog_categories),
    path('categories/<slug:slug>/', category_detail),
    # Теги
    path('tags/', catalog_tags),
    path('tags/<slug:slug>/', tag_detail),
    # Посты
    path('', post_detail),
    path('<slug:slug>/', catalog_posts),
]