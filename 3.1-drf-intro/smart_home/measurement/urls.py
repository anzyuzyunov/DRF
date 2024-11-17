from django.urls import path

from measurement.views import SensorView, SensViewOne, AllInf, MesInf, SensorCreate, SensorUpdate, MesCreate, SensorSet
from rest_framework.routers import DefaultRouter
r = DefaultRouter()
r.register('sensor_new', SensorSet)

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensor_up/<pk>/', SensorUpdate.as_view()),
    path('sensors_inf/', AllInf.as_view()),
    path('MesInf/', MesInf.as_view()),
    path('sensor/<pk>/', SensViewOne.as_view()),
    path('sensor_cr/', SensorCreate.as_view()),
    path('mes_cr/', MesCreate.as_view()),
] + r.urls
