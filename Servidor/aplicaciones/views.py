from django.shortcuts import render
import requests
from .forms import CrearPaciente

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

def verPacientes(request):
   url_api_replit = 'https://api-tareas.nicon607.repl.co/api/Paciente/'  # Reemplaza con la URL real

   response = requests.get(url_api_replit)

   if response.status_code == 200:
       data = response.json()
       # Procesa los datos como sea necesario
       return render(request, 'aplicaciones/probandoapirest.html', {'data': data})
   else:
       return render(request, 'error.html')
   
def crearPaciente(request):
    if request.method == 'POST':
        form = CrearPaciente(request.POST)
        if form.is_valid():
            data = {
                'rutPaciente': form.cleaned_data['rutPaciente'],
                'nomPaciente': form.cleaned_data['nomPaciente'],
                'apePaciente': form.cleaned_data['apePaciente'],
                'correo': form.cleaned_data['correo'],
                'contraPaciente': form.cleaned_data['contraPaciente'],
                'fechaNacimiento': form.cleaned_data['fechaNacimiento']
            }

            url_api_replit = 'https://api-tareas.nicon607.repl.co/api/Paciente/add'

            response = requests.post(url_api_replit, json=data)

            if response.status_code == 201:
                # La hora médica se creó con éxito
                return render(request, 'aplicaciones/InicioSesion.html')
            else:
                # Manejar el error de creación de hora médica
                return render(request, 'error.html')
    else:
        form = CrearPaciente()

    return render(request, 'aplicaciones/CrearCuenta', {'form': form})
