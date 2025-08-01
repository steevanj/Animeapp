# anime_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animecontents.urls')),
    path('users/', include('users.urls')),
]
