#William Andrés Gómez Roa
#@willandru
#26/06/2024

'''
Muestra en pantalla la configuración actual del dispositivo y permite encontrar la frecuencia de muestreo
que se desee y seleccionar los filtros que sirvan para dicha frecuencia de muestreo. Además, permite visualizar
los IDS de los filtros, el factor de escala actual, la impedancia de los canales, así como seleccionar la frecuencia 
de muestreo y el número de escaneos.

Este archivo es usado para buscar los parametros de configuración que se requieran en los otros scripts.
'''


import pygds 

d = pygds.GDS()

#Selecciona en 'Sampling Rate' y 'Number of Scans'
f_s_2 = sorted(d.GetSupportedSamplingRates()[0].items())[6]
d.SamplingRate, d.NumberOfScans = f_s_2
print(d.GetSupportedSamplingRates())
print(f_s_2)

#Buscar los filtros 
N = [x for x in d.GetNotchFilters()[0] if x['SamplingRate']
         == d.SamplingRate]
BP = [x for x in d.GetBandpassFilters()[0] if x['SamplingRate']
          == d.SamplingRate]
print('NOTHC ', N[1]) # index 9
print('BAND PASS', BP[9]) #index 123

#Factor de Escala
print(d.GetScaling())

# Finaliza la conexion con el dispositivo g-tec
d.Close()
del d