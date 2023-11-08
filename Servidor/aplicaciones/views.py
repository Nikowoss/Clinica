from django.shortcuts import render,redirect
import requests, json
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.


def CrearCuenta(request):
    return render(request,'aplicaciones/CrearCuenta.html')
    
def InicioMedico(request):
    return render(request,'aplicaciones/InicioMedico.html')    
    
def InicioPaciente(request):
    return render(request,'aplicaciones/InicioWebPaciente.html')

def HoraMedica(request):
    return render(request,'aplicaciones/HoraMedica.html')

def HoraDisponible(request):
    return render(request,'aplicaciones/HoraDisponible.html')

def CrearCuenta(request):
    return render(request,'aplicaciones/CrearCuenta.html')

def VistaMedico(request):
    correo = request.session.get('correo')
    return render(request, 'aplicaciones/VistaMedico.html', {'correo': correo})


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


def getEspecialidades(request):
    api_url = 'https://api-tareas.nicon607.repl.co/api/Especialidad'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        especialidades = [{'id': especialidad['idespecialidad'], 'nombre': especialidad['nomespecialidad']} for especialidad in data]
        print("Especialidades:", especialidades)
        return especialidades
    else:
        return []

    

def getMedicos(request):
    api_url = 'https://api-tareas.nicon607.repl.co/api/Medico'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        medicos = [{'nombre': medico['nommedico'], 'apellido': medico['apemedico']} for medico in data]
        print("Nombres de Medicos:", medicos)
        return medicos
    else:
        return []


def getCentros(request):
    api_url = 'https://api-tareas.nicon607.repl.co/api/Centro'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        nombres_centros = [( centro['nombrecentro']) for centro in data]
        print("Nombres de centros:", nombres_centros)
        return nombres_centros
    else:
        return []


def HoraMedica(request):
    especialidades = getEspecialidades(request)
    medicos = getMedicos(request)
    centros = getCentros(request)
    return render(request, 'aplicaciones/HoraMedica.html', {'especialidades': especialidades, 'medicos': medicos, 'centros': centros})



# # Vistas en Django
# from django.http import JsonResponse

# def obtener_medicos_y_centros(request, idespecialidad):
#     medicos = obtener_medicos_por_especialidad(idespecialidad)
#     centros = obtener_centros_por_especialidad(idespecialidad)

#     data = {
#         'medicos': medicos,
#         'centros': centros,
#     }

#     return JsonResponse(data)

# def obtener_medicos_por_especialidad(idespecialidad):
#     api_url = f'https://api-tareas.nicon607.repl.co/api/Medico?especialidad_idespecialidad={idespecialidad}'  # Asegúrate de usar el nombre correcto del campo
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         data = response.json()
#         medicos = [{'rutmedico': medico['rutmedico'], 'nombre': medico['nommedico']} for medico in data]
#         return medicos
#     else:
#         return []

# def obtener_centros_por_especialidad(especialidad_id):
#     api_url = f'https://api-tareas.nicon607.repl.co/api/Centro?especialidad_idcentro={especialidad_id}'  # Asegúrate de usar el nombre correcto del campo
#     response = requests.get(api_url)
    
#     if response.status_code == 200:
#         data = response.json()
#         centros = [{'idcentro': centro['idcentro'], 'nombrecentro': centro['nombrecentro']} for centro in data]
#         return centros
#     else:
#         return []


def loginMedico(request):
    print("a")
    api_url = 'https://api-tareas.nicon607.repl.co/api/Medico/login'

    print("Vista de inicio de sesión está siendo ejecutada")

    if request.method == 'POST':
        print("metodo post")
        usuario_data = {
            "correoMedico" : str(request.POST.get('correoMedico')),
            "contramedico" : str(request.POST.get('contramedico')),

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
                    correo = respuesta.get("correoMedico")
                    request.session['correo'] = correo
                    print("Inicio de sesión correcto")
                    print(correo)
                    print("Respuesta de la API:", respuesta)
                    return redirect('VistaMedico')
            else:
                print("Credenciales inválidas")
        except Exception as ex:
            print("Error en :", ex)
    return render(request,'aplicaciones/InicioMedico.html')
