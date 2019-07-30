from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models


'''
Movies
'''
class MovieListView(ListView):

    model = models.Movie
    template_name = 'movie/list.html'

    # def get_queryset(self):
    #     return models.Movie.objects.filter(year__gte=1995)

'''
Movie
'''
class MovieDetailView(DetailView):

    model = models.Movie
    template_name = 'movie/detail.html'