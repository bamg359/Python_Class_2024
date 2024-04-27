



edades= [34, 45, 19, 23, 37]

print(type(edades))

print(dir(edades))

print(edades)

print(len(edades))

print(edades[2])

edades[3]= 67

print(edades)

edades.append(45)

print(edades)
edades.pop(3)
print(edades)
#
print("el 45 aparece:",edades.count(45))
edades.remove(45)

print(edades)
edades.clear()
print(edades)



datos_cliente = []

nombre= input("Ingrese el nombre")

datos_cliente.append(nombre)

