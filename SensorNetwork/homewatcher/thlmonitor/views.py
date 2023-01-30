from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
import ast


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
        return HttpResponse("Received")
    if request.method == "GET":
        return HttpResponse("Server :)")
