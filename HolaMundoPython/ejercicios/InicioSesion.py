


##Registro

name = input("Ingrese su nombre: ")
email = input("Ingrese su email: ")
phone = input("Ingrese su telefono: ")
password= input("registre un password")



## Inicio de sesion

print("Iniciar Sesion: ")

users= input("Ingrese el email registrado o el telefono")

passuser= input("Ingrese su contraseña")

if((email == users or phone== users) and password== passuser):
    print(f"Bienvenido {name}")

else:
    print("Valide sus credenciales")
