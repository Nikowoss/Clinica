from django.urls import path
from .views import InicioSesion,InicioPaciente,CrearCuenta,HoraMedica,HoraDisponible,verPacientes,login

urlpatterns = [
    path('InicioSesion', login ,name="InicioSesion"),
    path('', InicioPaciente,name="InicioPaciente"),
    path('CrearCuenta',CrearCuenta,name="CrearCuenta"),
    path('HoraMedica',HoraMedica,name="HoraMedica"),
    path('HoraDisponible',HoraDisponible,name="HoraDisponible"),
    #path('probandoapirest',probandoapirest,name="probandoapirest"),
    path('verPacientes',verPacientes, name='verPacientes'),
]