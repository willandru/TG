#William Andrés Gómez Roa
#@willandru
#26/06/2024

'''
Protocolo de comunicación TCP/IP entre un servidor en python y un cliente en Labview.
Se adquieren señales EMG por medio de la conexión USB con el dispositivo g.USBamp-Research utilizando la librería 'pygds'
Los datos adquiridos son enviados por medio de protocolo TCP/IP a la aplicación de Labview; python envía los datos como servidor
y Labview los recibe como cliente.
'''

#COMUNICACIÓN DE LOS DATOS ADQUIRIDOS POR EL EQUIPO g-tec EN PYTHON A UNA APLICACIÓN DE LABVIEW

import socket
import struct
import numpy as np
import pygds
import time

HOST = 'localhost'
PORT = 1234

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Servidor escuchando en {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"Conexión establecida desde {addr}")

        try:
            #Loop de adquisición de la señal EMG y trasmisión de los datos
            while True:
                data = d.GetData(d.SamplingRate, more=lambda s: False)
                flattened_data = data.flatten()
                print(flattened_data)
                data_bytes = struct.pack(f"!{len(flattened_data)}d", *flattened_data)
                conn.sendall(data_bytes)


                # Lee el estado de la conexión
                conn.settimeout(1)
                '''
                try:
                    stop_signal = conn.recv(1)
                    if stop_signal.decode('utf-8') == 'Q':
                        print("Recibido señal de parada. Cerrando conexión.")
                        break
                except socket.timeout:
                    pass
                '''

        except Exception as e:
            print(f"Error durante la transmisión de datos: {e}")
        finally:
            print("Cerrando conexión...")
            conn.close()

if __name__ == "__main__":

    #Configurar el dispositivo G.TEC g.USBamp-Research
    d = pygds.GDS()

    #Activar los los canales y los filtros
    for i, channel in enumerate(d.Channels):
        if i == 0:
            channel.Acquire = 1
            channel.BandpassFilterIndex = 123
            channel.NotchFilterIndex = 9
        else:
            channel.Acquire = 0

    #Selecciona en 'Sampling Rate' y 'Number of Scans'
    f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6]
    d.SamplingRate, d.NumberOfScans = f_s_2

    #Aumenta la escala del algún canal.
    current_scaling = d.GetScaling()
    current_scaling[0].ScalingFactor = [1000.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    d.SetScaling(current_scaling)


    #Establece la configuración en el dispositivo g-tec
    d.SetConfiguration()

    #Inicia la adquisición de la señal EMG y empieza el servidor a trasmitir los datos al cliente en Labview
    start_server()

    #Finaliza la conexión - se detiene o cancela el programa
    d.Close()
    del d
