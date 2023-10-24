from django.shortcuts import render,redirect
import requests, json
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.


def InicioSesion(request):
    """  if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = {
                'rutPaciente': rutPaciente,
                'contraPaciente': contraPaciente
            }
            url_api_replit = 'https://api-tareas.nicon607.repl.co/api/Paciente/'

            response = requests.post(url_api_replit, json=data)

            # Obtén los datos del formulario
            rutPaciente = form.cleaned_data['rutPaciente']
            contraPaciente = form.cleaned_data['contraPaciente']

            # Realiza una solicitud a tu API para verificar el inicio de sesión
            
            response = requests.post(url_api_replit, json=data)

            if response.status_code == 200:
                # El inicio de sesión fue exitoso
                # Puedes personalizar la lógica para manejar el inicio de sesión
                return render(request,'InicioWebPaciente.html')  # Redirige a la página de inicio
            else:
                # El inicio de sesión falló
                # Puedes mostrar un mensaje de error en el formulario o redirigir a una página de error
                return render(request, 'InicioSesion.html')
    else:
        form = LoginForm()
"""
    return render(request, 'aplicaciones/InicioSesion.html')

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
    print("Estoy en crear")
    api_url = 'https://api-tareas.nicon607.repl.co/api/Paciente/add'

    print("Vista Crear")

    if request.method == 'POST':
        print("metodo post")
        usuario_data = {
            "rutPaciente" : str(request.POST.get('rutPaciente')),
            "nomPaciente" : str(request.POST.get('nomPaciente')),
            "apePaciente" : str(request.POST.get('apePaciente')),
            "correo" : str(request.POST.get('correo')),
            "contraPaciente" : str(request.POST.get('contraPaciente')),
            "fechaNacimiento" : str(request.POST.get('fechaNacimiento'))
    }
        print("Datos del usuario:", usuario_data)

        data_json = json.dumps(usuario_data)

        headers = {'Content-Type' : 'application/json'}

        try:
            response = requests.post(api_url, data=data_json, headers=headers)
            print(response)
            print("Estado de la respuesta:", response.status_code)
            if response.status_code == 200:
                respuesta = response.json()

                if respuesta.get("message") :
                    messages.warning(request, "Error al CrearCuenta")
                else:
                    print("Inicio de sesión correcto")
                    print("Respuesta de la API:", respuesta)
                    return redirect('HoraMedica')
            else:
                print("Credenciales inválidas")
        except Exception as ex:
            print("Error en :", ex)
    return render(request,'aplicaciones/CrearCuenta.html')

def login(request):
    print("a")
    api_url = 'https://api-tareas.nicon607.repl.co/api/Paciente/login'

    print("Vista de inicio de sesión está siendo ejecutada")

    if request.method == 'POST':
        print("metodo post")
        usuario_data = {
            "correo" : str(request.POST.get('correo')),
            "contraPaciente" : str(request.POST.get('contraPaciente'))
    }
        print("Datos del usuario:", usuario_data)

        data_json = json.dumps(usuario_data)

        headers = {'Content-Type' : 'application/json'}

        try:
            response = requests.post(api_url, data=data_json, headers=headers)
            print(response)
            print("Estado de la respuesta:", response.status_code)
            if response.status_code == 200:
                respuesta = response.json()

                if respuesta.get("message") :
                    messages.warning(request, "Error al iniciar sesión")
                else:
                    print("Inicio de sesión correcto")
                    print("Respuesta de la API:", respuesta)
                    return redirect('HoraMedica')
            else:
                print("Credenciales inválidas")
        except Exception as ex:
            print("Error en :", ex)
    return render(request,'aplicaciones/InicioSesion.html')