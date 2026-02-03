from django.urls import path

from film_manager.views import (
 FilmCreateView, FilmListView,
 FilmUpdateView, FilmDeleteView
)

urlpatterns = [
    path('create/', FilmCreateView.as_view(), name='film_create'),
    path('list/', FilmListView.as_view(), name="film_list"),
    path('delete/<int:pk>', FilmDeleteView.as_view(), name='film_delete'),
    path('edit/<int:pk>', FilmUpdateView.as_view(), name='film_edit'),
]