from django.contrib import admin
from django.urls import path, include
import posts.urls as posts_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('posts/', include(posts_urls)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
]
