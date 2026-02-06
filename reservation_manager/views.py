from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from reservation_manager.models import Reservation


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class ReservationListView(StaffRequiredMixin, ListView):
    model = Reservation
    template_name = 'dashboard/reservations/reservation_list.html'
    context_object_name = 'reservations'
    paginate_by = 10
    ordering = ['-created_at']


class ReservationDetailView(StaffRequiredMixin, DetailView):
    model = Reservation
    template_name = 'dashboard/reservations/reservation_detail.html'
    context_object_name = 'reservation'
