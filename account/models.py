from django.db import models

from core.models import BaseModel


# Create your models here.


class Client(BaseModel):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    class Meta:
        indexes = [models.Index(fields=['email'])]
    def __str__(self):
        return f"{self.prenom} {self.nom}"


