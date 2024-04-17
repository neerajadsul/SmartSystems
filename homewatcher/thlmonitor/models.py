from django.db import models


class EnvironmentalData(models.Model):
    """Represents environmental monitoring data from T, H, Lux sensors"""
    temperature = models.FloatField(verbose_name='Temperature')
    humidity = models.FloatField(verbose_name='Relative Humidity')
    lux_ir = models.IntegerField(verbose_name='IR Intensity')
    lux_vis_ir = models.IntegerField(verbose_name='Visible+IR Intensity')
    location = models.ForeignKey('SensorLocation', on_delete=models.PROTECT)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f'''location:{self.location}, Timestamp:{self.timestamp},T:{self.temperature},RH:{self.humidity},IR:{self.lux_ir}, VIS+IR:{self.lux_vis_ir}'''


class SensorLocation(models.Model):
    grid_coordinates = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.grid_coordinates