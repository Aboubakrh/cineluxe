from django.db import models

# Create your models here.
class Film(models.Model):
    tire = models.CharField(max_length=255)
    duree = models.PositiveIntegerField(help_text="Durée en munites")
    genre = models.CharField(max_length=255)
    realisateur = models.CharField(max_length=255)
    synopsis = models.TextField()
    affiche = models.ImageField(upload_to='films/', null=True, blank=True)
    def __str__(self):
        return self.tire
