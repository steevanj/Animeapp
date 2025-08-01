from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('anime/<int:anime_id>/', views.detail, name='detail'),
    path('filter/', views.filter_anime, name='filter'),
]
