# APP URLS
from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_categories, catalog_tags, catalog_posts, category_detail, tag_detail, post_detail

urlpatterns = [
    # Категории
    path('categories/', catalog_categories),
    path('categories/<slug:category_slug>/', category_detail),
    # Теги
    path('tags/', catalog_tags),
    path('tags/<slug:tag_slug>/', tag_detail),
    # Посты
    path('', catalog_posts),
    path('<slug:post_slug>/', post_detail),
    
]