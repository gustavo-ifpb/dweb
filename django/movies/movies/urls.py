"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.movie import views as movie

urlpatterns = [
    path('admin/', admin.site.urls),

    path('category/new/', movie.CategoryCreateView.as_view(), name='category-create'),

    path('movies/', movie.MovieListView.as_view(), name='movie-list'),
    path('movies/new/', movie.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', movie.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/edit/', movie.MovieUpdateView.as_view(), name='movie-edit'),
    path('movies/<int:pk>/delete/', movie.MovieDeleteView.as_view(), name='movie-delete'),
]
