from django.urls import path

from film_manager.views import (
    FilmCreateView, FilmListView,
    FilmUpdateView, FilmDeleteView, FilmDetailView,
    ClientFilmListView
)

urlpatterns = [
    path('create/', FilmCreateView.as_view(), name='film_create'),
    path('list/', FilmListView.as_view(), name="film_list"),
    path('detail/<uuid:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('delete/<uuid:pk>', FilmDeleteView.as_view(), name='film_delete'),
    path('edit/<uuid:pk>', FilmUpdateView.as_view(), name='film_update'),
    path('tous/', ClientFilmListView.as_view(), name='client_film_list'),
]