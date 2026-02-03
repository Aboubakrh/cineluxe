from django.contrib import admin

from cinema_manager.models import Cinema


# Register your models here.
@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    pass