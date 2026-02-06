from django.db import models

from core.models import BaseModel


# Create your models here.

class Salle(BaseModel):
    TYPE_ECRAN_CHOICES = [
        ('STD', 'Standard'),
        ('IMAX', 'IMAX'),
        ('3D', 'Real 3D'),
        ('4DX', '4DX'),
    ]
    cinema = models.ForeignKey('cinema_manager.Cinema', on_delete=models.CASCADE, related_name='cinemas')
    numero = models.PositiveIntegerField()
    capacite = models.PositiveIntegerField()
    type_ecran = models.CharField(max_length=20, choices=TYPE_ECRAN_CHOICES, default='STD')
 
    class Meta:
        indexes = [models.Index(fields=['numero'])]
    def __str__(self):
        return f" Salle {self.numero} | {self.cinema.nom}"

