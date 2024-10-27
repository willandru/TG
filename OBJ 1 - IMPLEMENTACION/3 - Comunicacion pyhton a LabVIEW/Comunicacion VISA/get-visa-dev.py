import pyvisa

rm = pyvisa.ResourceManager()
resources = rm.list_resources()

print("Connected VISA resources:")
for resource in resources:
    print(resource)
