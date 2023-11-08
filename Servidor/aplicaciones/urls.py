from django.urls import path
<<<<<<< HEAD
from .views import login,InicioPaciente,enviar_cliente_a_api,disponibilidad,loginMedico,CDPrueba,HoraMedica,HoraDisponible,verPacientes,vistaMedico,agenda,agregaragenda
=======
from .views import enviar_correo, login,InicioPaciente,enviar_cliente_a_api,HoraMedica,HoraDisponible,verPacientes,vistaMedico,disponibilidad
>>>>>>> seeeb

urlpatterns = [
    path('InicioSesion', login,name="InicioSesion"),
    path('', InicioPaciente,name="InicioPaciente"),
    path('CrearCuenta',enviar_cliente_a_api,name="CrearCuenta"),
    path('HoraMedica',HoraMedica,name="HoraMedica"),
    path('HoraDisponible',HoraDisponible,name="HoraDisponible"),
    #path('probandoapirest',probandoapirest,name="probandoapirest"),
    path('verPacientes',verPacientes, name='VerPacientes'),
    path('VistaMedico', vistaMedico, name='VistaMedico'),
<<<<<<< HEAD
    path('agenda', agenda, name='agenda'),
    path('agregaragenda', agregaragenda, name='agregaragenda'),
    path('CDPrueba', CDPrueba, name='CDPrueba'),
    path('InicioMedico', loginMedico, name='InicioMedico'),
    path('disponibilidad',disponibilidad,name='disponibilidad'),
    path('cargar-excel/', disponibilidad, name='cargar_excel'),
=======
    path('disponibilidad',disponibilidad,name='disponibilidad'),
    path('cargar-excel/', disponibilidad, name='cargar_excel'),
    path('EnviarCorreo',enviar_correo, name='enviar_correo'),

>>>>>>> seeeb
]