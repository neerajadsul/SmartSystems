from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('sensor_data', view=views.sensor_data, name='sensor_data'),
]