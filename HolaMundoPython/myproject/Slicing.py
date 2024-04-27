



edades= [34, 45, 19, 23, 37, 45 , 65, 42, 24]

#Slicing

print(edades[0:10])


# Toma todos los valores desde la posisión indicada
print(edades[1:])

#Va desde la posision 0 hasta donde se le indique menos 1
print(edades[:6])

print(edades[:-2])

print(edades[-9:])

edades.reverse()

print(edades)
#Podemos ordenar los valores
edades.sort(reverse=True)
print(edades)