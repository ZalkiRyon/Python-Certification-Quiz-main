import random

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

sueldos = []
afp = []
salud = []
liquido = []

for i in range(10):
    sueldo = random.randint(100, 1000)
    sueldos.append(sueldo)
    
for i in range(10):
    afp.append(sueldos[i] * 0.1)
    salud.append(sueldos[i] * 0.07)
    liquido.append(sueldos[i] - afp[i] - salud[i])

zipObj = zip(trabajadores, sueldos, afp, salud, liquido)
dictObj = list(zipObj)

print(dictObj)
