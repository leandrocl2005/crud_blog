from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# para desenvolvimento apenas
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
