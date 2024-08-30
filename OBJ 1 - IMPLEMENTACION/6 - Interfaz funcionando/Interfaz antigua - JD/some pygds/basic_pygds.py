import pygds

d = pygds.GDS() # " No device Found "

impedance = d.GetImpedance()

print(d)


#d.TriggerEnabled == d.Trigger == TriggerLinesEnabled == 


#The configuration names are unified
#FOR 1 DEVICE, the configuration fields are members of the device object:

d.Trigger = True
d.SetConfiguration()

#FOR MORE DEVICES

for c in d.Configs:
    c.Trigger=True
d.SetConfiguration()

#TO CONFIGURE ALL AVAILABLE CHANNELS 
pygds.configure_demo(d, testsignal=1)
d.SetConfiguration()

#TO ACQUIRE A FIXED NUMBER OF SAMPLES 
a= d.GetData(d.SamplingRate)
# a.shape[0] == d.SamplingRate    >>>True
    

#TO ACQUIRE A DYNAMIC NUMBER OF SAMPLES, PROVIDE A FUNCTION 'more(samples)'
#A pygds.Scope object can be used as a 'more' parameter of GetData()

scope = pygds.Scope(1/d.SamplingRate, title="Channels: %s", ylabel= u"U[\u03bcV]")
a= d.GetData(d.SamplingRate//2, scope)
del scope
a.shape[1]>=d.N_electrodes # >>>True

#TO REMOVE A GDS OBJECT MANUALLY:

d.Close()
del d

#---------------------------------------------------------------------------------------------
#-------------------------------CLASES--------------------------------------------------------

#--- BUILTINS---
builtins.Exception(builtins.BaseException) #GDSError
builtins.list(builtins.object) #ConnectedDevices
builtins.object #Scope
_config_wrap(__fi_struct_wrap) #GDS


#------CLASS  

class ConnectedDevices(builtins.list)
    # Lists all connected devices in a list of type "[(serial, devicetype, inuse)]"

    import pygds
    cd = pygds.ConnectedDevices() #This is used by the pygds.GDS Constructor . Use it separately only if
    # u do not want to instantiate a pygds.GDS object, but still want to find out wich devices are connected

    #METHOD RESOLUTION ORDER: 
        ConnectedDecives
        builtins.list
        builtins.object
    #METHODS DEFINED HETE
    __del__(self)
    __init__(self, server_ip='127.0.0.1') #Initialize self -> See help(type(self)) 
    find(self, wanted_type, exclude_serial=None)
        ConnectedDevices
    # TO FIND A DEVICE BY TYPE
        import pygds
        cd = pygds.ConnectedDecives()
        hiamp = cd.find(pygds.DEVICE_TYPE_GHIAMP)
        hiamp is None or len(hiamp.split('.'))>0    #True

    #DATA DESCRIPTORS
    __dict__ #dictionary for instance variables (if defined)
    __weakref__ #list of weak references to the object (if defined)

    #METHODS INHERITED FROM builtins.list:

    __add__(self, value, /) #Retrun self+value
    __contains__(self, key, /) #Return key in self
    __delitem__(self, key, /) #Delete self[key]
    __eq__(self, value, /) #Return self==value
    __ge__(self, value, /) #Return self >= value
    __getattribute__(self, name, /) # Return getattr(self, name)
    __getitem__(...) # x.__getitem__(y) <==> x[y]
    __gt__(self, value, /) #Return self>value
    __iadd__(self, value, /) #Implement self+=value
    __imul__(self, value, /) #Implement self*=value
    __iter__(self, /) #Implment iter(self)
    __le__(self, value, /) # Return self<=value
    __len__(self, /) #Return len self
    __lt__(self, value, /) # Return self<value
    __mul__(self, value, /) #Rerutn self*value.n
    __ne__(self, value, /) # Return self!=value
    __new__(*args, **kwargs) from builtins.type #Create and return a new object. See help(type)
    __repr__(self, /) # Return repr(self)
    __reversed__(...) #L.__reversed__() -- return a reverse iterator over the list
    __rmul__(self, value, /) # Return self*value
    __setitem__(self, key, value,) #Set self[key] to value
    __sizeof__(...) #L.__sizeof__() -- size of L in memory, in bytes
    append(...) #L.append(object) -> None -- append object to end
    clear(...) #L.clear() -> None -- remove all items from L
    copy(...) #L.copy() -> list -- a shallow copy of L
    count(...) #L.count(value) -> integer -- return number of occurrences of value
    extend(iterable) #L.extend() -> None -- extend list by appending elements from the iterable
    index(...) #L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present
    insert(...) #L.insert(index, object) -- insert object before index
    pop(...) #L.pop([index]) -> item --remove and return item at index (default last). Raise IndexError if list is empty or index is out of reange
    remove(...) #L.remove(value) -> None -- remove first occurrence of value . Raises ValueError if the value is not present.
    reverse(...) #L.reverse() -- reverse *IN PLACE*
    sort(...) #L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*

    #DATA AND OTHER ATTRIBUTES INHERITED FROM builtsins.list

    __hash__ = None

class GDS(_config_wrap)
    #The 'pygds.GDS' class initializes the connection to g.NEEDacces server

    #The constructor: 
        - Initializes the ocnnection to the wanted device(s)
        - Fetches the configuration(s)

    #  *gds_device*: can be
        - omitted (default)
        - the first letter of the serial
        - one of DEVICE_TYPE_GUSBAMP, DEVICE_TYPE_GHIAMP, DEVICE_TYPE_GNAUTILUS
        - a single serial
        - comma-separeted serial 
    #   *exclude_serials* : a list or set of serials to ignore. Default: None.
    #   *server_ip*: the IP addressof the GDS server. Default: pygds.SERVER_IP
        - The g.Needacces server port is pygds.SERVER_PORT and it is fixed
        - The client by default is pygds.CLIENT_IP and pygds.CLIEN_PORT. For a remote "server_ip", the local IP is automatically determined.

    #Without parameters the local host g.NEEDaccess server is used and the fisrt available device is connected.

    For one device the configuration fields are members of the GDS object.
    For more devices, every configuration is an entry in the "Configs" member.

    #-------g.USBamo configuration-----------------
    