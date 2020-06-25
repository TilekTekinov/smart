from django.db import models


class Sensor(models.Model):
    lamp = models.IntegerField(verbose_name='Lamp')
    socket = models.IntegerField(verbose_name='Socket')
    temperatura = models.FloatField(verbose_name='Temperatura')
    humidity = models.FloatField(verbose_name='Humidity')
    gas = models.FloatField(verbose_name='Gas')
    smoke = models.FloatField(verbose_name='Smoke')
