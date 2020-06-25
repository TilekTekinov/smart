from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('android_update/', views.androidUpdateData, name="androidUpdateData"),
    path('arduino_update/', views.arduinoUpdateData, name="arduinoUpdateData"),
    path('android_set/', views.androidSetData, name="androidSetData"),
    path('arduino_set/', views.arduinoSetData, name="arduinoSetData"),

]