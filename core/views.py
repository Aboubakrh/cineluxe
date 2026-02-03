from django.shortcuts import render
from django.views.generic import TemplateView

from film_manager.models import Film
from reservation_manager.models import Reservation
from salle_manager.models import Salle


# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        context['total_films'] = Film.objects.count()
        context['total_salles'] = Salle.objects.count()

        # Donnée victives
        context['revenu_total'] = "42 850"
        context['taux_occupation'] = 78.5
        context['reservations'] = Reservation.objects.select_related('client', 'film').order_by('-created_at')[:5]
        return context

