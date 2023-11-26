from django.shortcuts import render,redirect
import requests, json
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
import json
import calendar
import datetime
import pandas as pd
from django.core.mail import send_mail

# Create your views here.
def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = 'tu_correo@gmail.com'
        destinatario = [request.POST['destinatario']]

        send_mail(asunto, mensaje, remitente, destinatario, fail_silently=False)

        return HttpResponse('Correo enviado exitosamente.')

    return render(request, 'aplicaciones/EnviarCorreo.html') 
    
def disponibilidad(request):
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        if excel_file.name.endswith('.xls') or excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file)
            
            # Aquí puedes procesar los datos del DataFrame (df) como desees
            # Por ejemplo, puedes guardarlos en la base de datos o realizar algún otro cálculo.
            columnas_mostrar = ['Estado','Fecha','Hora Inicio', 'Hora Final'] #Aqui se agregan los campos a mostrar

            df_mostrar = df[columnas_mostrar]

            # Convierte el DataFrame en una tabla HTML
            tabla_html = df_mostrar.to_html(classes='table table-bordered', escape=False, index=False)

            return render(request, 'aplicaciones/resultado.html', {'data': tabla_html})
        else:
            return render(request, 'aplicaciones/error.html', {'error_message': 'El archivo no es un archivo Excel válido.'})
    return render(request, 'aplicaciones/disponibilidad.html')

def resultado(request):
    api_url = 'https://api-tareas.nicon607.repl.co/api/disponibilidad/add'

    
    return render(request,'aplicaciones/resultado.html')


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

def agenda(request):
    
    ##AQUI HACER QUE CARGUEN LAS AGENDA DE ESE MEDICO
    return render(request,'aplicaciones/agenda.html')

def CDPrueba(request):
    
    
    
    
    return render(request,'aplicaciones/CDPrueba.html')

def agregaragenda(request):

    print("Estoy en agregargenda")
    api_url = 'https://api-tareas.nicon607.repl.co/api/Agenda/add'
    url_api_replit = 'https://api-tareas.nicon607.repl.co/api/a/Id' 

    response = requests.get(url_api_replit)

    if response.status_code == 200:
        data = response.json()
        json_data = json.dumps(data)
        parsed_data = json.loads(json_data)
        idagenda = parsed_data[0]['idagenda']
        idagedarial = idagenda+1
    print("Vista Crear")

    if request.method == 'POST':
        a = datetime.strptime(request.POST.get("fechainicio"), '%Y-%m-%d')
        fecha_formateada = a.strftime('%m-%d-%Y')
        b = datetime.strptime(request.POST.get("fecha_final"), '%Y-%m-%d')
        fecha_formateadb = b.strftime('%m-%d-%Y')
        print(fecha_formateada)
        print("metodo post")
        agendadata = {
            "idagenda" : idagedarial,
            "fechainicio" : (fecha_formateada),
            "fecha_final" : (fecha_formateadb),
            "medico_rutmedico" : str(request.POST.get('medico_rutmedico'))
    }
        print("Datos de la agenda:", agendadata)

        data_json = json.dumps(agendadata)

        headers = {'Content-Type' : 'application/json'}

        try:
            response = requests.post(api_url, data=data_json, headers=headers)
            print(response)
            print("Estado de la respuesta:", response.status_code)
            if response.status_code == 200:
                respuesta = response.json()

                if respuesta.get("message") :
                    messages.warning(request, "Error al agendar")
                else:
                    print("AgendaCreada")
                    print("Respuesta de la API:", respuesta)
                    return redirect('agenda')
            else:
                print("Ingresa bien las was po oeeeee ")
        except Exception as ex:
            print("Error en :", ex)
    
    
    
    return render(request,'aplicaciones/agregaragenda.html')
def loginMedico(request):
    print("a")
    api_url = 'https://api-tareas.nicon607.repl.co/api/Medico/login'

    print("Vista de inicio de sesión está siendo ejecutada")

    if request.method == 'POST':
        print("metodo post")
        correo = request.POST.get('correoMedico')
        print(correo)
        usuario_data = {
            "correoMedico" : str(correo),
            "contramedico" : str(request.POST.get('contramedico')),

    }
        print("Datos del usuario:", usuario_data)
        correo = request.POST.get('correoMedico')
        print(correo)

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
                    print("Respuesta de la API:", respuesta)
                    print(correo)
                    return redirect('VistaMedico')
            else:
                print("Credenciales inválidas")
        except Exception as ex:
            print("Error en :", ex)
    return render(request,'aplicaciones/InicioMedico.html')

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
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = 'tu_correo@gmail.com'
        destinatario = [request.POST['destinatario']]

        send_mail(asunto, mensaje, remitente, destinatario, fail_silently=False)
        
    url_api_replit = 'https://api-tareas.nicon607.repl.co/api/Paciente/'  # Reemplaza con la URL real

    response = requests.get(url_api_replit)

    if response.status_code == 200:
        data = response.json()
        # Procesa los datos como sea necesario
        return render(request, 'aplicaciones/probandoapirest.html', {'data': data})
    else:
        return render(request, 'aplicaciones/error.html')

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