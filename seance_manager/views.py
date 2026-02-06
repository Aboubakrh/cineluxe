from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from seance_manager.models import Seance


class SeanceListView(ListView):
    model = Seance
    template_name = 'dashboard/seances/seance_list.html'
    context_object_name = 'seances'
    paginate_by = 10
    ordering = ['-created_at']


class SeanceCreateView(CreateView):
    model = Seance
    fields = ['film', 'salle', 'date_heure', 'prix']
    template_name = 'dashboard/seances/form_seance.html'
    success_url = reverse_lazy('seance_list')


class SeanceUpdateView(UpdateView):
    model = Seance
    fields = ['film', 'salle', 'date_heure', 'prix']
    template_name = 'dashboard/seances/form_seance.html'
    success_url = reverse_lazy('seance_list')


class SeanceDeleteView(DeleteView):
    model = Seance
    template_name = 'dashboard/seances/seance_confirm_delete.html'
    success_url = reverse_lazy('seance_list')