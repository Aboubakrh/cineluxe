
from django.db import models

from core.models import BaseModel


# Create your models here.
class Cinema(BaseModel):
    nom = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)

    def __str__(self):
        return  f'{self.nom} | {self.ville}'
    class Meta:
        indexes = [models.Index(fields=['nom'])]
        verbose_name = 'Cinéma'
        verbose_name_plural = 'Cinemas'


