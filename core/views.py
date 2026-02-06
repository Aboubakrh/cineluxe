from django.shortcuts import render
from django.views.generic import TemplateView

from film_manager.models import Film
from reservation_manager.models import Reservation
from salle_manager.models import Salle


# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    
    def test_func(self):
        return self.request.user.is_staff
    def get_context_data(self, **kwargs):
        from django.db.models import Sum, F, DecimalField, ExpressionWrapper
        from django.utils import timezone
        
        context = super(DashboardView, self).get_context_data(**kwargs)

        # Totals
        context['total_films'] = Film.objects.count()
        context['total_salles'] = Salle.objects.count()
        
        # Real Stats
        total_revenue = Reservation.objects.aggregate(
            total=Sum(
                ExpressionWrapper(
                    F('nb_places') * F('seance__prix'),
                    output_field=DecimalField()
                )
            )
        )['total'] or 0
        context['revenu_total'] = total_revenue
        
        # Active Seances (future)
        from seance_manager.models import Seance
        context['seances_active'] = Seance.objects.filter(date_heure__gte=timezone.now()).count()
        
        # Recent Reservations
        context['reservations'] = Reservation.objects.select_related('client', 'seance__film', 'seance__salle__cinema').order_by('-created_at')[:5]
        
        return context

