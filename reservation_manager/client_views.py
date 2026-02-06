from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView
from django.urls import reverse
from .forms import ReservationForm
from .models import Reservation
from seance_manager.models import Seance
from account.models import Client

class ClientReservationCreateView(FormView):
    template_name = 'client/reservation_form.html'
    form_class = ReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seance_id = self.kwargs.get('seance_id')
        context['seance'] = get_object_or_404(Seance, pk=seance_id)
        return context

    def form_valid(self, form):
        seance_id = self.kwargs.get('seance_id')
        seance = get_object_or_404(Seance, pk=seance_id)
        
        data = form.cleaned_data
        
        # Get or Create Client
        client, created = Client.objects.get_or_create(
            email=data['email'],
            defaults={
                'nom': data['nom'],
                'prenom': data['prenom'],
                'telephone': data['telephone']
            }
        )
        
        # Update client info if exists (optional, but good practice)
        if not created:
            client.nom = data['nom']
            client.prenom = data['prenom']
            client.telephone = data['telephone']
            client.save()

        # Create Reservation
        reservation = Reservation.objects.create(
            client=client,
            seance=seance,
            nb_places=data['nb_places']
        )
        
        # Redirect to success page or detail
        return render(self.request, 'client/reservation_success.html', {'reservation': reservation})
