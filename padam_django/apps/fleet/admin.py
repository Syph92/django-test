
# Django import.
from django.contrib import admin

# App import
from . import models
from .forms import BusStopForm


@admin.register(models.BusStop)
class BusStopAdmin(admin.ModelAdmin):
    form = BusStopForm
    list_display = ('uid', 'driver', 'bus', 'time_stop',)

@admin.register(models.Bus)
class BusAdmin(admin.ModelAdmin):
    pass 
@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
