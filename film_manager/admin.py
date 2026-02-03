from django.contrib import admin

from film_manager.models import Film


# Register your models here.

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
 pass