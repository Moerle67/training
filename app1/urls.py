from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name = "start"),
    path('anmeldung/<str:rtn_name>', views.anmeldung, name = "anmeldung"),
    path('abmeldung/<str:rtn_name>', views.abmeldung, name = "abmeldung"),
]
