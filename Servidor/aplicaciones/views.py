from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from django.contrib import messages

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
        'rutPaciente': '12345', ##ACA DARLE LOS DATOS DEL FORM EN CREARCUENTA.HTML
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

    ##ACA IRIA LA WEA DE HEADER O UNA WEA ASI QUE ES LO QUE DA PROBLEMA DE MODULO

    # Verifica si la solicitud fue exitosa
    if response.status_code == 200:
        return HttpResponse("Cliente enviado con éxito a la API Flask")
    else:
        return HttpResponse("Error al enviar el cliente a la API Flask", status=500)

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
                    #messages.success(request, "Paciente: " + respuesta.get ("correo")+ "Inicio sesión")
                    return redirect('HoraMedica')
            else:
                print("Credenciales inválidas")
        except Exception as ex:
            print("Error en :", ex)
    return render(request,'aplicaciones/InicioSesion.html')