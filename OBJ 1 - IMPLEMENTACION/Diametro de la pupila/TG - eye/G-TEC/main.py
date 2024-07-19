import pygds

d = pygds.GDS()

print(d.GetSupportedSamplingRates())
minf_s = sorted(d.GetSupportedSamplingRates()[0].items())[5]
d.SamplingRate, d.NumberOfScans = minf_s
print(minf_s, '<-Frecuencia de muestreo y Número de escaneos')

for ch in d.Channels:
    print('ch: ', ch)
    
    ch.Acquire = True
d.SetConfiguration() 
data = d.GetData(d.SamplingRate)

print('Data: ', data)
print("Shape:", data.shape)
