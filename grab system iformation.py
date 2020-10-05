import wmi



#for windown wmi
c = wmi.WMI()
myOs = c.Win32_ComputerSystem()[0]

print(f'Manufacturer: {myOs.Manufacturer}')
print(f'model: {myOs.model}')

#for linux use platform

