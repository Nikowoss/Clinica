from django.urls import path
from .views import login,InicioPaciente,enviar_cliente_a_api,perfil,VerHoraMedica,enviar_correo,disponibilidad,loginMedico,CDPrueba,HoraMedica,HoraDisponible,verPacientes,vistaMedico,agenda,agregaragenda

urlpatterns = [
    path('InicioSesion', login,name="InicioSesion"),
    path('', InicioPaciente,name="InicioPaciente"),
    path('CrearCuenta',enviar_cliente_a_api,name="CrearCuenta"),
    path('HoraMedica',HoraMedica,name="HoraMedica"),
    path('HoraDisponible',HoraDisponible,name="HoraDisponible"),
    #path('probandoapirest',probandoapirest,name="probandoapirest"),
    path('verPacientes',verPacientes, name='VerPacientes'),
    path('VistaMedico', vistaMedico, name='VistaMedico'),
    path('agenda', agenda, name='agenda'),
    path('agregaragenda', agregaragenda, name='agregaragenda'),
    path('CDPrueba', CDPrueba, name='CDPrueba'),
    path('InicioMedico', loginMedico, name='InicioMedico'),
    path('disponibilidad',disponibilidad,name='disponibilidad'),
    path('cargar-excel/', disponibilidad, name='cargar_excel'),
    path('EnviarCorreo/', enviar_correo, name='enviar_correo'),
    path('VerHoraMedica/', VerHoraMedica, name='VerHoraMedica'),
    path('perfil/', perfil, name='perfil'),
]