from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from salle_manager.models import Salle


class SalleListView(ListView):
    model = Salle
    template_name = 'dashboard/salles/salle_list.html'
    context_object_name = 'salles'
    paginate_by = 10
    ordering = ['-created_at']


class SalleCreateView(CreateView):
    model = Salle
    fields = ['cinema', 'numero', 'capacite', 'type_ecran']
    template_name = 'dashboard/salles/form_salle.html'
    success_url = reverse_lazy('salle_list')


class SalleUpdateView(UpdateView):
    model = Salle
    fields = ['cinema', 'numero', 'capacite', 'type_ecran']
    template_name = 'dashboard/salles/form_salle.html'
    success_url = reverse_lazy('salle_list')


class SalleDeleteView(DeleteView):
    model = Salle
    template_name = 'dashboard/salles/salle_confirm_delete.html'
    success_url = reverse_lazy('salle_list')
