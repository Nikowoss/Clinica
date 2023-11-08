from django.urls import path
from .views import login, InicioPaciente, enviar_cliente_a_api, HoraMedica, HoraDisponible, verPacientes, loginMedico, InicioMedico, VistaMedico

urlpatterns = [
    path('InicioSesion', login, name="InicioSesion"),
    path('', InicioPaciente, name="InicioPaciente"),
    path('CrearCuenta', enviar_cliente_a_api, name="CrearCuenta"),
    path('VistaMedico', VistaMedico, name='VistaMedico'),
    path('HoraMedica', HoraMedica, name="HoraMedica"),
    path('HoraDisponible', HoraDisponible, name="HoraDisponible"),
    path('verPacientes', verPacientes, name='VerPacientes'),
    path('InicioMedico', loginMedico, name='InicioMedico'),
    #path('probandoapirest',probandoapirest,name="probandoapirest"),
    # path('obtener_medicos_y_centros/<int:especialidad_id>/', views.obtener_medicos_y_centros, name='obtener_medicos_y_centros'),
]