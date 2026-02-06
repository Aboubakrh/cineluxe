from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from cinema_manager.models import Cinema


class CinemaListView(ListView):
    model = Cinema
    template_name = 'dashboard/cinemas/cinema_list.html'
    context_object_name = 'cinemas'
    paginate_by = 10
    ordering = ['-created_at']


class CinemaCreateView(CreateView):
    model = Cinema
    fields = ['nom', 'adresse', 'ville']
    template_name = 'dashboard/cinemas/form_cinema.html'
    success_url = reverse_lazy('cinema_list')


class CinemaUpdateView(UpdateView):
    model = Cinema
    fields = ['nom', 'adresse', 'ville']
    template_name = 'dashboard/cinemas/form_cinema.html'
    success_url = reverse_lazy('cinema_list')


class CinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'dashboard/cinemas/cinema_confirm_delete.html'
    success_url = reverse_lazy('cinema_list')
