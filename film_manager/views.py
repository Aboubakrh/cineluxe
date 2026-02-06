from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView, DetailView

from film_manager.models import Film

class FilmCreateView(CreateView):
    model = Film
    fields = ["titre", "duree", "genre", "realisateur", "synopsis", "affiche"]
    template_name = 'dashboard/films/form_film.html'
    success_url = reverse_lazy('film_list')

class FilmListView(ListView):
    model = Film
    fields = ["id","titre", "duree", "genre", "realisateur", "affiche"]
    template_name = 'dashboard/films/films_list.html'
    context_object_name = 'films'
    paginate_by = 5

class FilmUpdateView(UpdateView):
    model = Film
    fields = ["titre", "duree", "genre", "realisateur", "affiche"]
    template_name = 'dashboard/films/form_film.html'
    success_url = reverse_lazy('film_list')

class FilmDeleteView(DeleteView):
    model = Film
    template_name = 'dashboard/films/film_confirm_delete.html'
    success_url = reverse_lazy('film_list')
    def get(self, request, *args, **kwargs):
        return self.post(request,*args, **kwargs)

class FilmDetailView(DetailView):
    model = Film
    template_name = 'client/film_detail.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seances'] = self.object.seances.order_by('date_heure')
        return context
