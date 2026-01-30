import uuid

from django.core.validators import MinValueValidator

from django.db import models

from core.models import BaseModel


# Create your models here.

class Reservation(BaseModel):
    client = models.ForeignKey('account.Client', on_delete=models.CASCADE, related_name='reservations')
    seance = models.ForeignKey('seance_manager.Seance', on_delete=models.CASCADE, related_name='reservations')
    date_reservation = models.DateTimeField(auto_now_add=True)
    nb_places = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    @property
    def total_prix(self):
        return self.nb_places * self.seance.prix

    def __str__(self):
        return f"Réservation {self.id} - {self.client.nom}"