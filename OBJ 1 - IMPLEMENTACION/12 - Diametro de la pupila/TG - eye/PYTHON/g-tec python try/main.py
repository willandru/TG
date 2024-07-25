import pygds

d = pygds.GDS() # " No device Found "

impedance = d.GetImpedance()

print(d)
print('Impedance : ', impedance)