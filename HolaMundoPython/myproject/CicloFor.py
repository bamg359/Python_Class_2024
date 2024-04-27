

edades= [34, 45, 19, 23, 37, 45 , 65, 42, 24]

print( "in")
for edad in edades:
    print(edad)
print("Usando indices")
for i in range(len(edades[2:6])):
    print("Dato ",i,":",edades[i])


claves=("Nombre: ", "Apellido: ", "Correo: ","clave:")
datos = []

for i in range(len(claves)):
    dato = input("Ingrese el valor")
    datos.append(dato)


for clave, dato in zip(claves, datos):
    print(f"{clave}:{dato}")