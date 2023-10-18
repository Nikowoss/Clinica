from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.


def InicioSesion(request):
    return render(request,'aplicaciones/InicioSesion.html')

def CrearCuenta(request):
    return render(request,'aplicaciones/CrearCuenta.html')
    
def InicioPaciente(request):
    return render(request,'aplicaciones/InicioWebPaciente.html')

def HoraMedica(request):
    return render(request,'aplicaciones/HoraMedica.html')

def HoraDisponible(request):
    return render(request,'aplicaciones/HoraDisponible.html')

def CrearCuenta(request):
    return render(request,'aplicaciones/CrearCuenta.html')
def vistaMedico(request):
    return render(request, 'aplicaciones/vistaMedico.html')

def verPacientes(request):
   url_api_replit = 'https://api-tareas.nicon607.repl.co/api/Paciente/'  # Reemplaza con la URL real

   response = requests.get(url_api_replit)

   if response.status_code == 200:
       data = response.json()
       # Procesa los datos como sea necesario
       return render(request, 'aplicaciones/probandoapirest.html', {'data': data})
   else:
       return render(request, 'error.html')

def enviar_cliente_a_api(request):
    # Datos del cliente que deseas enviar
    cliente_data = {
        'rutPaciente': '12345',
        'nomPaciente': 'John',
        'apePaciente': 'Doe',
        'correo': 'john@example.com',
        'contraPaciente': 'contrasena',
        'fechaNacimiento': '2000-01-01'
    }

    # URL de la API Flask
    api_url = 'https://api-tareas.nicon607.repl.co/api/Paciente/add'  # Reemplaza con la URL real de tu API

    # Realiza una solicitud POST a la API Flask
    response = requests.post(api_url, json=cliente_data)

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        return HttpResponse("Cliente enviado con éxito a la API Flask")
    else:
        return HttpResponse("Error al enviar el cliente a la API Flask", status=500)
