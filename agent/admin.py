from django.contrib import admin
from .models import *

class SightingAdmin(admin.ModelAdmin):
    model = Sighting
    list_display = ['timestamp', 'device_id', 'signal_dbm']

admin.site.register(Sighting, SightingAdmin)
