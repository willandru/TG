#William Andrés Gómez Roa
#@willandru
#26/06/2024
'''
Permite configurar uno o más canales al aplicarles 2 filtros que se escogieron con ayuda del el script
'buscarConfiguracion.py' y aumentar el factor de escala para cada canal. Una vez establecida la configuración
del dispositivo, se utiliza la terminal para mostrar 5 datos adquiridos, además se muestra el tamaño de los datos.
'''

import pygds 

d = pygds.GDS()

#Selecciona en 'Sampling Rate' y 'Number of Scans'
f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6]
d.SamplingRate, d.NumberOfScans = f_s_2

# Activar un canal específico
for i, channel in enumerate(d.Channels):
    if i == 0:
        channel.Acquire = 1
        channel.BandpassFilterIndex = 123
        channel.NotchFilterIndex = 9
    else:
        channel.Acquire = 0

# Aumentar la escala del algún canal.
current_scaling = d.GetScaling()
current_scaling[0].ScalingFactor = [100.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
d.SetScaling(current_scaling)


#Fija la configuración anterior en el dispositivo
d.SetConfiguration()

# IMPRIME POR LA TERMINAL 5 MUESTRAS DE DATOS

#Funcion para manejar la adquisicion de los datos y el manejo de los mismos
samples_received = 0
max_samples = 5  # Numero de muestras por recibir
def print_samples(s):
    global samples_received
    samples_received += 1
    print(s.flatten())
    print(s.shape)
    return samples_received < max_samples  # Permite enviar solo 5 muestras

# Loop de adquisición de la señal EMG
while True:
    data = d.GetData(d.SamplingRate, more=print_samples)
    if samples_received >= max_samples:
        break

# Finaliza la conexion con el dispositivo g-tec
d.Close()
del d