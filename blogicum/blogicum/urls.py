from django.contrib import admin
from django.urls import path

from blog import views as blog_views
from pages import views as pages_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='index'),
    path('posts/<int:id>/', blog_views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         blog_views.category_posts,
         name='category_posts'),
    path('pages/about/', pages_views.about, name='about'),
    path('pages/rules/', pages_views.rules, name='rules')
]
