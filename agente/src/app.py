import requests
import platform
import psutil

def process_to_dict(process):
    return {
        'pid': process.pid,
        'name': process.name(),
        'status': process.status()
    }

def send_system_info():
    url = 'http://localhost:7000/data'  # Reemplazar con direccion de ec2 manteniendo el puerto o en caso de modificarlo hacerlo primero en la API

    # Obtengo información del sistema
    processes = [process_to_dict(p) for p in psutil.process_iter()]
    users = [u._asdict() for u in psutil.users()]

    system_info = {
        'processor': platform.processor(),
        'processes': processes,
        'users': users,
        'os_name': platform.system(),
        'os_version': platform.release()
    }

    # Envio la información al endpoint /data de la API
    try:
        response = requests.post(url, json=system_info)
    except requests.exceptions.ConnectionError as e:
        print("Ocurrió un error de conexión:", e)
    
    if response.status_code == 200:
        print('Información enviada exitosamente')
    else:
        print('Error al enviar la información:', response.status_code)

send_system_info()
