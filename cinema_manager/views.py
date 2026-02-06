from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cinema_manager.models import Cinema


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class CinemaListView(StaffRequiredMixin, ListView):
    model = Cinema
    template_name = 'dashboard/cinemas/cinema_list.html'
    context_object_name = 'cinemas'
    paginate_by = 10
    ordering = ['-created_at']


class CinemaCreateView(StaffRequiredMixin, CreateView):
    model = Cinema
    fields = ['nom', 'adresse', 'ville']
    template_name = 'dashboard/cinemas/form_cinema.html'
    success_url = reverse_lazy('cinema_list')


class CinemaUpdateView(StaffRequiredMixin, UpdateView):
    model = Cinema
    fields = ['nom', 'adresse', 'ville']
    template_name = 'dashboard/cinemas/form_cinema.html'
    success_url = reverse_lazy('cinema_list')


class CinemaDeleteView(StaffRequiredMixin, DeleteView):
    model = Cinema
    template_name = 'dashboard/cinemas/cinema_confirm_delete.html'
    success_url = reverse_lazy('cinema_list')
