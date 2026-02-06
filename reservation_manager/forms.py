from django import forms
from django.core.validators import MinValueValidator

class ReservationForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Nom")
    prenom = forms.CharField(max_length=100, label="Prénom")
    email = forms.EmailField(label="Email")
    telephone = forms.CharField(max_length=20, label="Téléphone")
    nb_places = forms.IntegerField(min_value=1, label="Nombre de places")
