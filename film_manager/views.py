from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from film_manager.models import Film

class FilmCreateView(CreateView):
    model = Film
    fields = ["tire", "duree", "genre", "realisateur", "synopsis", "affiche"]
    template_name = 'dashboard/films/form_film.html'
    success_url = reverse_lazy('film_list')

class FilmListView(ListView):
    model = Film
    fields = ["id","tire", "duree", "genre", "realisateur", "affiche"]
    template_name = 'dashboard/films/films_list.html'
    context_object_name = 'films'

class FilmUpdateView(UpdateView):
    model = Film
    fields = ["tire", "duree", "genre", "realisateur", "affiche"]
    template_name = 'dashboard/films/form_film.html'
    success_url = reverse_lazy('film_list')

class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('film_list')
    def get(self, request, *args, **kwargs):
        return self.post(request,*args, **kwargs)
