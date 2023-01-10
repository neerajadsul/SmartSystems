from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime


def index(request):
    context = {
        'time':datetime.now(),
    }
    return render(request, 'thlmonitor/index.html' ,context)

