from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from seance_manager.models import Seance


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class SeanceListView(StaffRequiredMixin, ListView):
    model = Seance
    template_name = 'dashboard/seances/seance_list.html'
    context_object_name = 'seances'
    paginate_by = 10
    ordering = ['-created_at']


class SeanceCreateView(StaffRequiredMixin, CreateView):
    model = Seance
    fields = ['film', 'salle', 'date_heure', 'prix']
    template_name = 'dashboard/seances/form_seance.html'
    success_url = reverse_lazy('seance_list')


class SeanceUpdateView(StaffRequiredMixin, UpdateView):
    model = Seance
    fields = ['film', 'salle', 'date_heure', 'prix']
    template_name = 'dashboard/seances/form_seance.html'
    success_url = reverse_lazy('seance_list')


class SeanceDeleteView(StaffRequiredMixin, DeleteView):
    model = Seance
    template_name = 'dashboard/seances/seance_confirm_delete.html'
    success_url = reverse_lazy('seance_list')