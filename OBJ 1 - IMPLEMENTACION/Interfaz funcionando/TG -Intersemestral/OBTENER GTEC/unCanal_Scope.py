#William Andrés Gómez Roa
#@willandru
#26/06/2024
'''
Permite configurar uno o más canales al aplicarles 2 filtros que se escogieron con ayuda del el script
'buscarConfiguracion.py' y aumentar el factor de escala para cada canal. Una vez establecida la configuración
del dispositivo, se utiliza un osciloscopio para mostrar la señal en vivo.
'''
import pygds 

#Incializa un objeto que representa al dispositivo g.USBamp 
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
current_scaling[0].ScalingFactor = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
d.SetScaling(current_scaling)

print(d.GetScaling())
#Fija la configuración anterior en el dispositivo
d.SetConfiguration()


# Muestra un Osciloscopio en vivo de la señal

scope = pygds.Scope(1/d.SamplingRate) 
d.GetData(d.SamplingRate,scope)



