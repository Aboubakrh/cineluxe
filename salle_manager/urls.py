from django.urls import path
from salle_manager.views import (
    SalleListView, SalleCreateView,
    SalleUpdateView, SalleDeleteView
)

urlpatterns = [
    path('list/', SalleListView.as_view(), name='salle_list'),
    path('create/', SalleCreateView.as_view(), name='salle_create'),
    path('edit/<uuid:pk>/', SalleUpdateView.as_view(), name='salle_update'),
    path('delete/<uuid:pk>/', SalleDeleteView.as_view(), name='salle_delete'),
]
