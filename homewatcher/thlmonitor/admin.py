from django.contrib import admin

from .models import EnvironmentalData, SensorLocation

admin.site.register(SensorLocation)
admin.site.register(EnvironmentalData)
