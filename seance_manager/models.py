from django.db import models

from core.models import BaseModel


# Create your models here.
class Seance(BaseModel):
    film = models.ForeignKey('film_manager.Film', on_delete=models.CASCADE, related_name='seances')
    salle = models.ForeignKey('salle_manager.Salle', on_delete=models.CASCADE, related_name='seances')
    date_heure = models.DateTimeField()
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.film.titre} @ {self.date_heure.strftime('%d/%m %H:%M')}"
