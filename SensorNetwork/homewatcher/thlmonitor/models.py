from django.db import models


class EnvironmentalData(models.Model):
    """Represents environmental monitoring data from T, H, Lux sensors"""
    temperature = models.FloatField(verbose_name='Temperature')
    humidity = models.FloatField(verbose_name='Relative Humidity')
    lux_ir = models.IntegerField(verbose_name='IR Intensity')
    lux_vis_ir = models.IntegerField(verbose_name='Visible+IR Intensity')
    location = models.ForeignKey('SensorLocation', on_delete=models.PROTECT)


class SensorLocation(models.Model):
    class Floor(models.IntegerChoices):
        GROUND = 0
        FIRST = 1

    class GridColumn(models.TextChoices):
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'
        F = 'F'

    class GridRow(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7

    floor = models.IntegerField(choices=Floor.choices)
    grid_column = models.CharField(max_length=2, choices=GridColumn.choices)
    grid_rows = models.IntegerField(choices=GridRow.choices)
    simple_name = models.CharField(max_length=32)