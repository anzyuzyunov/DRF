from rest_framework import serializers

from .models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы

class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        # depth = 1
        # fields = ['id','name','description', 'sensors_inf']
        fields = ['id','name','description']
        # fields = '__all__'
        write_only = True
        many = True

    # def save(self, **kwargs):
    #     name = self.validated_data['name']
    #     description = self.validated_data['description']

class MeasurementSerializer(serializers.ModelSerializer):
    # sensor_id = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all(), source='sensors_inf', write_only=True)

    class Meta:
        model = Measurement
        fields = ['sensors','date_of_measurement','temperature']
        write_only = True

class SensorDetailSerializer(serializers.ModelSerializer):

    sensors_inf = MeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'sensors_inf',]


class NewSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensors', 'temperature']

