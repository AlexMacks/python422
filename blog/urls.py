# MAIN URLS
from django.contrib import admin
from django.urls import path
from python_blog.views import main
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main, name="main"),
    path('posts/', include('python_blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
