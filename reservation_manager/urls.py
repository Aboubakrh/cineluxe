from django.urls import path
from reservation_manager.views import (
    ReservationListView, ReservationDetailView
)
from reservation_manager.client_views import ClientReservationCreateView

urlpatterns = [
    path('list/', ReservationListView.as_view(), name='reservation_list'),
    path('detail/<uuid:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('create/<uuid:seance_id>/', ClientReservationCreateView.as_view(), name='reservation_create'),
]
