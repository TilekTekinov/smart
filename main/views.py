import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Sensor


def index(request):
    return render(request, 'main/index.html')


def androidUpdateData(request):
    sensor = Sensor.objects.get(id=2)
    response_data = {
        'lamp': sensor.lamp,
        'socket': sensor.socket,
        'temperature': sensor.temperatura,
        'humidity': sensor.humidity,
        'gas': sensor.gas,
        'smoke': sensor.smoke,
    }

    print(response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def arduinoUpdateData(request):
    sensor = Sensor.objects.get(id=2)
    response_data = {
        'lamp': sensor.lamp,
        'socket': sensor.socket,
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def androidSetData(request):
    print(request.body)
    print(request.GET.get('lamp'))
    sensor = Sensor.objects.get(id=2)
    # sensor.socket = request.GET.get('socket')
    sensor.lamp = request.GET.get('lamp')
    sensor.save()
    return HttpResponse('<html><body>Success</body></html>')


@csrf_exempt
def arduinoSetData(request):
    if (json.loads(request.body)['values'][0] == json.loads(request.body)['values'][0] and json.loads(request.body)['values'][1] == json.loads(request.body)['values'][1]):
        sensor = Sensor.objects.get(id=2)
        sensor.temperatura = json.loads(request.body)['values'][0]
        sensor.humidity = json.loads(request.body)['values'][1]
        sensor.save()
    return HttpResponse('<html><body>Success</body></html>')
