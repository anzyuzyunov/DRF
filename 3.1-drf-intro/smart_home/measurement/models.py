from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=300, verbose_name='название датчика')
    description = models.CharField(max_length=2000, blank=True,null=True, verbose_name='описание датчика')


    class Meta():

        def __str__(self):
            return self.name

class Measurement(models.Model):
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensors_inf')
    temperature = models.FloatField(verbose_name='температура')
    date_of_measurement = models.DateTimeField(auto_now_add=True,verbose_name='дата и время измерения')





# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
