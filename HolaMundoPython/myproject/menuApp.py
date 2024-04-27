
nombre = ""
apellido = ""
correo = ""
contrasena = ""
peso = ""
altura =""



def registrar():
    global nombre, apellido, correo , contrasena
    nombre  = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    contrasena= input("Ingrese su contrasena: ")

def imprimir_info(iniciar_sesion):

    if iniciar_sesion== True:
        print(f"Nombre {nombre}\n apellido{apellido} \n"
            f"Correo{correo}")

def iniciar_sesion():
    correo_reg= input("Ingrese el correo registrado")
    contrasena_reg = input("Ingrese la contraseña registrada")

    if correo == correo_reg and contrasena == contrasena_reg:
        print(f"Bienvenido {nombre}")

        return True
    else:
        return False



init = int(input("Presione 1 para iniciar"))

while(init != 0):

    opc = int(input("Seleccione \n 1. Registrar \n 2.Inicio de Sesion \n 3. Salir"))

    if opc ==1:
        print("Registro")
        registrar()
    elif opc==2:
        print("Inicio de Sesión")
        imprimir_info(iniciar_sesion())
    elif opc == 3:
        print("salir")
        init = 0

