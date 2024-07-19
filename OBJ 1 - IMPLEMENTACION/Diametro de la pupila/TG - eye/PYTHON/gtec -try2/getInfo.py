import pygds

d = pygds.GDS()

methods_and_attributes = ['Calibrate', 'Channels', 'Close', 'CommonGround', 'CommonReference', 'ConfigCount', 'Configs', 'Counter', 'CounterEnabled', 'DI', 'DeviceType', 'GetAsyncDigitalIOs', 'GetAvailableChannels', 'GetAvailableDigitalIOs', 'GetBandpassFilters', 'GetChannelNames', 'GetConfiguration', 'GetData', 'GetDataInfo', 'GetDeviceInformation', 'GetFactoryScaling', 'GetImpedance', 'GetNetworkChannel', 'GetNotchFilters', 'GetScaling', 'GetSupportedInputSources', 'GetSupportedNetworkChannels', 'GetSupportedSamplingRates', 'GetSupportedSensitivities', 'IndexAfter', 'InternalSignalGenerator', 'IsCreator', 'N_ch_calc', 'N_electrodes', 'Name', 'NumberOfScans', 'NumberOfScans_calc', 'ResetScaling', 'SampleRate', 'SamplingRate', 'Serials', 'SetAsyncDigitalOutputs', 'SetConfiguration', 'SetNetworkChannel', 'SetScaling', 'ShortCutEnabled', 'Trigger', 'TriggerEnabled']

for item in methods_and_attributes:
    if hasattr(d, item):
        attr = getattr(d, item)
        if callable(attr):
            print(f"{item}: (method)")
            help(attr)
            print('*************')
        else:
            print(f"{item}: {attr} (attribute)")
            print('*************')
    else:
        print(f"{item}: (not found)")
