from django.urls import path
from seance_manager.views import (
    SeanceListView, SeanceCreateView,
    SeanceUpdateView, SeanceDeleteView
)

urlpatterns = [
    path('list/', SeanceListView.as_view(), name='seance_list'),
    path('create/', SeanceCreateView.as_view(), name='seance_create'),
    path('edit/<uuid:pk>/', SeanceUpdateView.as_view(), name='seance_update'),
    path('delete/<uuid:pk>/', SeanceDeleteView.as_view(), name='seance_delete'),
]
