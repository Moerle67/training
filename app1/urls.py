from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name = "start"),
    # Userverwaltung 
    path('anmeldung/<str:rtn_name>', views.anmeldung, name = "anmeldung"),
    path('abmeldung/<str:rtn_name>', views.abmeldung, name = "abmeldung"),
    path('newpwd/<str:rtn_name>', views.newpwd, name = "newpwd"),
    path('reg/<str:rtn_name>', views.reg, name = "reg"),
]
