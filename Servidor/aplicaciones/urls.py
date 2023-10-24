from django.urls import path
from .views import login,InicioPaciente,enviar_cliente_a_api,HoraMedica,HoraDisponible,verPacientes,vistaMedico

urlpatterns = [
    path('InicioSesion', login,name="InicioSesion"),
    path('', InicioPaciente,name="InicioPaciente"),
    path('CrearCuenta',enviar_cliente_a_api,name="CrearCuenta"),
    path('HoraMedica',HoraMedica,name="HoraMedica"),
    path('HoraDisponible',HoraDisponible,name="HoraDisponible"),
    #path('probandoapirest',probandoapirest,name="probandoapirest"),
    path('verPacientes',verPacientes, name='VerPacientes'),
    path('VistaMedico', vistaMedico, name='VistaMedico'),
]