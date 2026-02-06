from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from salle_manager.models import Salle


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class SalleListView(StaffRequiredMixin, ListView):
    model = Salle
    template_name = 'dashboard/salles/salle_list.html'
    context_object_name = 'salles'
    paginate_by = 10
    ordering = ['-created_at']


class SalleCreateView(StaffRequiredMixin, CreateView):
    model = Salle
    fields = ['cinema', 'numero', 'capacite', 'type_ecran']
    template_name = 'dashboard/salles/form_salle.html'
    success_url = reverse_lazy('salle_list')


class SalleUpdateView(StaffRequiredMixin, UpdateView):
    model = Salle
    fields = ['cinema', 'numero', 'capacite', 'type_ecran']
    template_name = 'dashboard/salles/form_salle.html'
    success_url = reverse_lazy('salle_list')


class SalleDeleteView(StaffRequiredMixin, DeleteView):
    model = Salle
    template_name = 'dashboard/salles/salle_confirm_delete.html'
    success_url = reverse_lazy('salle_list')
