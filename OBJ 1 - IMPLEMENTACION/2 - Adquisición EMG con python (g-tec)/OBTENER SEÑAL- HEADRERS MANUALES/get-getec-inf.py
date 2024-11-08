import pygds
import numpy as np
from scipy import io
from datetime import datetime

# Define the paths to the headers
gNEEDaccessHeaders = [
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gHIamp.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gNautilus.h",
    r"C:/Users/willa/OneDrive/Documents/gtec/gNEEDaccessClientAPI/C/GDSClientAPI_gUSBamp.h"
]
# Initialize pygds with headers
result = pygds.Initialize(gds_headers=gNEEDaccessHeaders)
print(result)

SERIALNUMBER = 'UR-2019.12.09'
d = pygds.GDS()
DISABLEREMOTEFEATURES = False
SAMPLINGRATE = 256
BLOCKSIZE = 8       # block size for GetData (data retrieval from GDS --> Python)
                    # integral value; should be an integral multiple of 'NUMBEROFSCANS' parameter (zero needs to be treated specially)

NUMBEROFSCANS = 0   # block size for amplifier (data transmission from device --> GDS)
                    # zero for default, values depending on sampling rate
FILENAME = 'RecordedData'
# define visualization constants
SHOWLASTXSECONDS = 1 

# define file name
datetimeStr = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = FILENAME + '_' + datetimeStr + '.mat'

# callback for each GetData cycle when the specified block size of samples was acquired
def GetDataCallback(dataBlock, filename, scope):
    samples = []
    
    # open the data file and append the latest block of data samples
    try:
        file = io.loadmat(filename, variable_names = ["data"])
        samples = file['data']
    except Exception as e:
        # Just print(e) is cleaner and more likely what you want,
        # but if you insist on printing message specifically whenever possible...
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)

    if len(samples) == 0:
        samples = np.vstack(dataBlock.copy())
    else:
        samples = np.vstack((samples, dataBlock.copy()))

    io.savemat(filename, {"data":samples})
    
    # VISUALIZATION OPTION A: show the last X seconds of the data
    continueDAQ = True
    s = len(samples)
    l = SHOWLASTXSECONDS*SAMPLINGRATE
    if (s % l == 0):
        continueDAQ = scope(samples[len(samples)-min(len(samples),SHOWLASTXSECONDS*SAMPLINGRATE):])
     
    # VISUALIZATION OPTION B: show only the latest datablock -> does not make sense for little BLOCKSIZE values
    #continueDAQ = scope(dataBlock)
    
    return continueDAQ



print('Configuring GDS for {0} usage ({1} remote features)...'.format('local-only' if DISABLEREMOTEFEATURES else 'default' , 'disabling' if DISABLEREMOTEFEATURES else 'enabling'))
pygds.Uninitialize()
pygds.Initialize(gds_dll = pygds.gds_dll_standalone if DISABLEREMOTEFEATURES else pygds.gds_dll_client)

print('Opening device...')
#d=pygds.GDS(SERIALNUMBER)
#d = pygds.GDS()


d.NumberOfScans = NUMBEROFSCANS
d.SamplingRate = SAMPLINGRATE
#d.CommonGround = [1] * 4
#d.CommonReference = [1] * 4
#d.ShortCutEnabled = 1
#d.CounterEnabled = 0
#d.TriggerEnabled = 1
'''
for ch in d.Channels:
    ch.Acquire = 1
    ch.BandpassFilterIndex = -1
    ch.NotchFilterIndex = -1
    ch.BipolarChannel = 0
'''
# Activate a specific channel
for i, ch in enumerate(d.Channels):
    if i == 0:
        ch.Acquire = 1
        ch.BandpassFilterIndex = -1
        ch.NotchFilterIndex = -1
        ch.NotchFilterIndex = -1
        ch.BipolarChannel = 0
    else:
        ch.Acquire = 0

d.SetConfiguration()

# create the visualization scope
scope = pygds.Scope(1 / SAMPLINGRATE, xlabel='t/s', ylabel='U/$\mu$V',
    title="{0} (%s channels)".format(SERIALNUMBER))

# start and run data acquisition loop (stops automatically when data viewer window is closed)
callback = lambda samples: GetDataCallback(samples, filename, scope) 
data = d.GetData(BLOCKSIZE, callback)

d.Close()
del d













'''
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

'''