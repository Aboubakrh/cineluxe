from django.urls import path
from cinema_manager.views import (
    CinemaListView, CinemaCreateView, 
    CinemaUpdateView, CinemaDeleteView
)

urlpatterns = [
    path('list/', CinemaListView.as_view(), name='cinema_list'),
    path('create/', CinemaCreateView.as_view(), name='cinema_create'),
    path('edit/<uuid:pk>/', CinemaUpdateView.as_view(), name='cinema_update'),
    path('delete/<uuid:pk>/', CinemaDeleteView.as_view(), name='cinema_delete'),
]
