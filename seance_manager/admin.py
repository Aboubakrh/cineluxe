from django.contrib import admin

from reservation_manager.models import Reservation
from seance_manager.models import Seance


# Register your models here.
@admin.register(Seance)
class SeanceAdmin(admin.ModelAdmin):
    pass