




user_name= "Pepito"

salary = 1300000

eps = salary * 0.04

pension = salary * 0.04

net_salary = salary - eps - pension

print(net_salary)

#calcular el iva de un producto

#En este caso input genera un str que se debe parsear para completar la operacion

precio = int(input("Ingrese el valor del precio: "))

tasa_iva = 0.19

iva_producto = precio * tasa_iva



print(iva_producto)

iva_to_string = str(iva_producto)

print(type(iva_to_string))

salute = " Hello world"

print(salute.upper())

print(salute.strip())

print(dir(salute))