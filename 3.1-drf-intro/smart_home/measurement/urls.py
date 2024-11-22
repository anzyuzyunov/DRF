from django.urls import path

from measurement.views import SensorCreate, SensorUpdate, MesCreate


urlpatterns = [
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('sensors/', SensorCreate.as_view()),
    path('measurements/', MesCreate.as_view()),

]
