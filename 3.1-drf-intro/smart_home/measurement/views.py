# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measurement

from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


# class SensorView(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer


class SensorCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


# class SensViewOne(RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

# class AllInf(ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer

#
# class MesInf(ListAPIView):
#     queryset = Measurement.objects.all()
#     serializer_class = MeasurementSerializer

class MesCreate(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


