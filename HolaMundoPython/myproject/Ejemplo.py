




users={}

def registrarUsuario():
    user = {}
    name = input("Ingrese el nombre")
    user.update({"name:" : name})
    last_name = input("Ingrese el apellido")
    user.update({"last_name:": last_name})
    doc = input("Ingrese su numero de cedula:" )
    email = input("Ingrese el correo")
    user.update({"Email:": email})
    salary = int(input("Ingrese el salario"))
    user.update({"salary:": salary})
    users.update({doc: user})


registrarUsuario()
registrarUsuario()
registrarUsuario()


print(users)



