from django.shortcuts import render,redirect
import requests, json
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime
import json
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
    url_api_replit = 'https://api-tareas-2.nicon607.repl.co/api/Modulo/add' 
    url_api = 'https://api-tareas-2.nicon607.repl.co/api/Disponibilidad/add' 
    
    if request.method == 'POST' and request.FILES['excel_file']:
        excel_file = request.FILES['excel_file']

        if excel_file.name.endswith('.xls') or excel_file.name.endswith('.xlsx'):
            df = pd.read_excel(excel_file)
            
            columnas_mostrar = ['Estado','Fecha','Hora Inicio', 'Hora Final'] #Aqui se agregan los campos a mostrar que coincidan en el excel

            df_mostrar = df[columnas_mostrar]
            
            #para tener las filas por separadas
            filas_lista = df[columnas_mostrar].values.tolist() 
            #obtener el rut del medico de la lista en el excel
            rut_lista = df['Rut Medico'].values.tolist()
            
            rut = rut_lista[0] # devuelve str
            print(rut)
            print(len(rut))
            #obtener los valores maximos de las id, evitando que se repitan claves primarias
            api = 'https://api-tareas-2.nicon607.repl.co/api/Modulo'
            response = requests.get(api)
            
            x = 0
            y = 0
            if response.status_code == 200:
                data = response.json()
                ids = [modulo['idmodulo'] for modulo in data]
                
                if ids:
                    x = max(ids)
                else:
                    x = 0
            else:
                x = 0
            api_v2 = 'https://api-tareas-2.nicon607.repl.co/api/Disponibilidad'
            response_v2 = requests.get(api_v2)
            if response_v2.status_code == 200:
                dat = response_v2.json()
                ids_v2 = [disponibilidad['id_disponibilidad'] for disponibilidad in dat]
                if ids_v2:
                    print("error aca antes")
                    y = max(ids_v2)
                    y = y + 1
                    print(y)
                else:
                    y = 1
                    print(y)
            else:
                y = 1
            #obtener al medico para verificar que este exista
            api_med = 'https://api-tareas-2.nicon607.repl.co/api/Medico'
            response_med = requests.get(api_med)
            rut_med_C = ""
            if response_med.status_code == 200:
                dat_med = response_med.json()
                rut_med_bd = [medicos['rutmedico'] for medicos in dat_med]
                print(rut_med_bd)
            if rut_lista[0] in rut_med_bd:
                rut_med_C = rut_lista[0]
                print(len(rut_med_C))
                print(rut_med_C)
                print("los ruts coinciden")
            #recorrer la matriz y mandar datos al replit
                for lista in filas_lista:
                    x = x + 1
                    y = y + 1
                    
                    lista_def = []  
                    #print(lista)
                    #print(x)
                    lista_def.append(x)
                    lista_def.append(str(lista[2]))
                    lista_def.append(str(lista[3]))
                    
                    #print(lista_def)
                    #tabla modulo
                    modulo_data = {
                        "idmodulo" : x,
                        "horaInicio" : str(lista[2]),
                        "horaFinal" : str(lista[3])
                    } 
                    #tabla disponibilidad
                    dispo_data = {
                        "id_disponibilidad" : y,
                        "modulo_idmodulo" : x,
                        "fechaDispon" : str(lista[1]),
                        "disponible" : str(lista[0]),
                        "rut_medico" : rut
                        }
    
                    # Convertir la lista de diccionarios a JSON
                    lista_def_json = json.dumps(modulo_data)
                    dispo_json = json.dumps(dispo_data)

                    # Enviar lista_def_json a la API
                    api_response = requests.post(url_api_replit, data=lista_def_json, headers={'Content-Type': 'application/json'})
                    # enviar dispo_json a la API
                    api_res = requests.post(url_api, data=dispo_json, headers={'Content-Type': 'application/json'})
                    #arreglar logica para ingresar la disponibilidad y el modulo, cual va primero
                    
                    print("Respuesta API Modulo:", api_response.status_code)
                    print("Respuesta API Disponibilidad:", api_res.status_code)

                    if api_res.status_code == 200:
                        print(api_res.status_code)
                    else:
                        print(api_res.status_code)
                        print("respuesta de disponibilidad mala")
                    if api_response.status_code == 200:
                        print(api_response.status_code)
                    else:
                        print(api_response.status_code)
                        print("respuesta de modulo mala")
                    
                # Convierte el DataFrame en una tabla HTML
                if api_response.status_code == 200:
                    return render(request, 'aplicaciones/resultado.html', {'data': df_mostrar.to_html(classes='table table-bordered', escape=False, index=False)})
                else:
                    messages.warning(request, f"Error al enviar datos a la API. Código de estado: {api_response.status_code}")
                tabla_html = df_mostrar.to_html(classes='table table-bordered', escape=False, index=False)

                return render(request, 'aplicaciones/resultado.html', {'data': tabla_html, 'filas_lista': filas_lista})
            else:
                print("rut no valido")
                return render(request, 'aplicaciones/error.html', {'error_message': 'El rut ingresado en el excel no esta registrado .'})
        else:
            return render(request, 'aplicaciones/error.html', {'error_message': 'El archivo no es un archivo Excel válido.'})
    return render(request, 'aplicaciones/disponibilidad.html')

def enviar_correo(request):
    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = 'tu_correo@gmail.com'
        destinatario = [request.POST['destinatario']]

        send_mail(asunto, mensaje, remitente, destinatario, fail_silently=False)

        return HttpResponse('Correo enviado exitosamente.')

    return render(request, 'aplicaciones/EnviarCorreo.html') 
def resultado(request):
    api_url = 'https://api_tareas-1.nicon607.repl.co/api/disponibilidad/add'

    
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
    
    url_api_replit = 'https://api-tareas-2.nicon607.repl.co/api/DisponibilidadNico/' 

    response = requests.get(url_api_replit)

    if response.status_code == 200:
        data = response.json()
        
        return render(request, 'aplicaciones/agenda.html', {'data': data})
    else:
        return render(request, 'aplicaciones/error.html')

def CDPrueba(request):
    
    
    
    
    return render(request,'aplicaciones/CDPrueba.html')

def agregaragenda(request):

    print("Estoy en agregargenda")
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Agenda/add'
    url_api_replit = 'https://api-tareas-2.nicon607.repl.co/api/a/Id' 

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
            "fechainicio" : str(fecha_formateada),
            "fecha_final" : str(fecha_formateadb),
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
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Medico/login'

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
        
    url_api_replit = 'https://api-tareas-2.nicon607.repl.co/api/Paciente/'  # Reemplaza con la URL real

    response = requests.get(url_api_replit)

    if request.method == 'POST':
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']
        remitente = 'tu_correo@gmail.com'
        destinatario = [request.POST['destinatario']]

        send_mail(asunto, mensaje, remitente, destinatario, fail_silently=False)
    if response.status_code == 200:
        data = response.json()
        # Procesa los datos como sea necesario
        return render(request, 'aplicaciones/probandoapirest.html', {'data': data})
    else:
        return render(request, 'aplicaciones/error.html')

def enviar_cliente_a_api(request):
    print("Estoy en crear")
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Paciente/add'
    
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
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Paciente/login'
    api_urlxdatospaci = 'https://api-tareas-2.nicon607.repl.co/api/Paciente/b'
    if request.method == 'POST':
        print("metodo post")
        correo = request.POST.get('correo')
        usuario_data = {
            "correo" : str(request.POST.get('correo')),
            "contraPaciente" : str(request.POST.get('contraPaciente'))
    }
        print("Datos del usuario:", usuario_data)

        data_json = json.dumps(usuario_data)

        headers = {'Content-Type' : 'application/json'}

        try:
            response = requests.post(api_url, data=data_json, headers=headers)
            response2 = requests.post(api_urlxdatospaci, json={'correo': correo})
            print(response)
            print(response2)
            print("Estado de la respuesta:", response.status_code)
            if response.status_code == 200:
                respuesta = response.json()
                disp = response2.json()
                if respuesta.get("message") :
                    messages.warning(request, "Error al iniciar sesión")
                else:
                    print(response2)
                    print("Inicio de sesión correcto")
                    print("Respuesta de la API:", respuesta)
                    especialidades = getEspecialidades(request)
                    medicos = getMedicos(request)
                    centros = getCentros(request)
                    request.session['disp'] = disp
                    return render(request, 'aplicaciones/HoraMedica.html', {'especialidades': especialidades, 'medicos': medicos, 'centros': centros, 'disp': disp})
            else:
                print("Credenciales inválidas")
        except Exception as ex:
            print("Error en :", ex)
    return render(request,'aplicaciones/InicioSesion.html')

def getEspecialidades(request):
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Especialidad'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        especialidades = [{'id': especialidad['idespecialidad'], 'nombre': especialidad['nomespecialidad']} for especialidad in data]
        return especialidades
    else:
        return []

    

def getMedicos(request):
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Medico'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        medicos = [{
            'rutmedico': medico['rutmedico'],
            'nombre': medico['nommedico'],
            'apellido': medico['apemedico'],
            'especialidad_idespecialidad': medico['especialidad_idespecialidad']
        } for medico in data]
        return medicos
    else:
        return []


def getCentros(request):
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/Centro'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        nombres_centros = [( centro['nombrecentro']) for centro in data]
        return nombres_centros
    else:
        return []
    
def VerHoraMedica(request):
    disp = request.session.get('disp', {})
    api_url = 'https://api-tareas-2.nicon607.repl.co/api/HoraMedica/add'
    url_api_replit = 'https://api-tareas-2.nicon607.repl.co/api/a/Id' 

    response = requests.get(url_api_replit)

    if response.status_code == 200:
        data = response.json()
        json_data = json.dumps(data)
        parsed_data = json.loads(json_data)
        idhoramedica = parsed_data[0]['idhoramedica']
        idhoramedicarial = idhoramedica+1
        
        if request.method == 'POST':
            idhoramedica = idhoramedicarial
            id_disponibilidad = request.POST.get("disponibilidad")
            paciente_rutpaciente = disp[0]['rutPaciente']
            estadoHora = True
            print(paciente_rutpaciente)
            Horadata = {
                "idhoramedica" : idhoramedica,
                "id_disponibilidad" : id_disponibilidad,
                "paciente_rutpaciente" :paciente_rutpaciente,
                "estadoHora" : estadoHora}
            print("Datos de la HoraMedica:", Horadata)

            data_json = json.dumps(Horadata)

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
                        noDisponible = "NODISPONIBLE"  
                        data_to_update = {'disponible': noDisponible}  
                        result = actualizar_disponibilidad(id_disponibilidad, data_to_update)
                        print(result)
                        print("AgendaCreada")
                        print("Respuesta de la API:", respuesta)
                        return redirect('perfil')
                else:
                    print("Ingresa bien las was po oeeeee ")
            except Exception as ex:
                print("Error en :", ex)
    return render(request,'aplicaciones/VerHoraMedica.html', {'disp': disp})

def perfil(request):
    disp = request.session.get('disp', {})
    try:
        if request.method == 'POST':
            paciente_rutpaciente = disp[0]['rutPaciente']
            print(paciente_rutpaciente)
            if paciente_rutpaciente :
                api_url = 'https://api-tareas-2.nicon607.repl.co/api/HoraMedicaNico/a'
                response = requests.post(api_url, json={'paciente_rutpaciente': paciente_rutpaciente})
                if response.status_code == 200:
                    dato = response.json()
                    return render(request, 'aplicaciones/HoraDisponible.html', {'dato': dato, 'disp': disp})
                else:
                    return render(request, 'aplicaciones/error.html', {'error_message': 'Error en la solicitud de disponibilidad'})
    except Exception as ex:
                print("Error en :", ex)
    return render(request, 'aplicaciones/perfil.html', {'disp': disp})

def actualizar_disponibilidad(id_disponibilidad, data_to_update):
    api_url = f'https://api-tareas-2.nicon607.repl.co/api/Disponibilidad/update/{id_disponibilidad}'
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.put(api_url, data=json.dumps(data_to_update), headers=headers)

        if response.status_code == 200:
            return {"msg": "Disponibilidad actualizada"}
        elif response.status_code == 404:
            return {"message": "No se encontró la disponibilidad para actualizar"}, 404
        else:
            return {"message": "Error en la actualización de disponibilidad"}, response.status_code
    except Exception as ex:
        return {"message": str(ex)}, 500
    
def HoraDisponible(request):
    try:
        if request.method == 'POST':
            rut_medico = request.POST.get('medico')
            especialidad = request.POST.get('especialidad')
            print(rut_medico)
            print(especialidad)
            if rut_medico != "Selecciona un médico":
                print(rut_medico)
                api_url = 'https://api-tareas-2.nicon607.repl.co/api/DisponibilidadNico/a'
                response = requests.post(api_url, json={'rut_medico': rut_medico})
                if response.status_code == 200:
                    
                    dato = response.json()
                    disp = request.session.get('disp', {})
                    datoDisp = request.session.get('datoDisp', {})
                    return render(request, 'aplicaciones/HoraDisponible.html', {'dato': dato, 'disp': disp, 'datoDisp': datoDisp})
                else:
                    return render(request, 'aplicaciones/error.html', {'error_message': 'Error en la solicitud de disponibilidad'})
            else:
                api_url = 'https://api-tareas-2.nicon607.repl.co/api/DisponibilidadNico/b'
                response = requests.post(api_url, json={'especialidad_idespecialidad': especialidad})
            if response.status_code == 200:
                dato = response.json()
                disp = request.session.get('disp', {})
                datoDisp = request.session.get('datoDisp', {})
                return render(request, 'aplicaciones/HoraDisponible.html', {'dato': dato, 'disp': disp, 'datoDisp': datoDisp})
            else:
                return render(request, 'aplicaciones/error.html', {'error_message': 'Error en la solicitud de disponibilidad'})

            
        else:
            return render(request, 'aplicaciones/error.html', {'error_message': 'Método no permitido'})
    except Exception as ex:
        return render(request, 'aplicaciones/error.html', {'error_message': str(ex)})


def HoraMedica(request):
    especialidades = getEspecialidades(request)
    medicos = getMedicos(request)
    centros = getCentros(request)
    return render(request, 'aplicaciones/HoraMedica.html', {'especialidades': especialidades, 'medicos': medicos, 'centros': centros})