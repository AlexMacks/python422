# APP URLS
from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_categories, catalog_tags, catalog_posts, category_detail, tag_detail, post_detail, post_create, tag_create, category_create, category_update
app_name = 'blog'

urlpatterns = [
    # Каталог  постов posts/
    path("", catalog_posts, name="posts"),
    # Категории
    # Категории posts/categories/
    # Категории posts/categories/python/
    path("categories/", catalog_categories, name="categories"),
    path("categories/create/", category_create, name="category_create"),
    path("categories/<slug:category_slug>/", category_detail, name="category_detail"),
    path(
        "categories/<slug:category_slug>/update/",
        category_update,
        name="category_update",
    ),
    # path('categories/<slug:category_slug>/delete/', category_detail, name='category_detail'),
    # Теги posts/tags/
    # Теги posts/tags/python/
    path("tags/", catalog_tags, name="tags"),
    path("tags/create/", tag_create, name="tag_create"),
    path("tags/<slug:tag_slug>/", tag_detail, name="tag_detail"),
    # Посты posts/
    path("create/", post_create, name="post_create"),
    path("<slug:post_slug>/", post_detail, name="post_detail"),
]