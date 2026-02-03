from django.contrib import admin

from film_manager.models import Film
from salle_manager.models import Salle


# Register your models here.

@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    pass