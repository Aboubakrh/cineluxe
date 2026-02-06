from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from reservation_manager.models import Reservation


class ReservationListView(ListView):
    model = Reservation
    template_name = 'dashboard/reservations/reservation_list.html'
    context_object_name = 'reservations'
    paginate_by = 10
    ordering = ['-created_at']


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'dashboard/reservations/reservation_detail.html'
    context_object_name = 'reservation'
