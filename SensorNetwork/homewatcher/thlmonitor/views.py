from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import time
import ast
from .models import EnvironmentalData, SensorLocation


def index(request):
    context = {
        'time':datetime.now(),
    }
    return render(request, 'thlmonitor/index.html' ,context)


@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        sbody = request.body.decode()
        data = ast.literal_eval(sbody)

        sensor_location = SensorLocation(grid_coordinates = data['location'])
        sensor_location.save()

        thl_data = EnvironmentalData(
            temperature=data['T'],
            humidity = data['RH'],
            lux_ir = data['LUX'][0],
            lux_vis_ir = data['LUX'][1],
            location = sensor_location,
            timestamp = datetime.fromtimestamp(data['timesecs'])
        )
        thl_data.save()

        return HttpResponse("Received")
    if request.method == "GET":
        print(time.time)
        return HttpResponse(f"{int(time.time())}")




