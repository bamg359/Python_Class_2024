






user = {

    "Name": "Pepito",
    "age": 26,
    "Salary": 1700000,
    "Role": "Developer",
    "IsActive:": True
}

## Los diccionarios son ordenados
print(user)
# Podemos acceder llamando la clave
print(user["Name"])

role = user.get("Role")

print(role)

user["Salary"] = 2500000

print(user["Salary"])

value = user.values()
print(value)

item = user.items()

print(item)

print(user.keys())

#in is

if "Salary" in user:
    print("Key Available")
else:
    print("Not Available")

user.update({"LastName:": "Perez", "email": "pp@mail.com"})

print(user.values())

for i in user:
    print(user[i])

for x in user.values():
    print(x)

for j,k in user.items():
    print(j,k)

# producto:  nombre , precio , costo , cantidad , categoria , subcategoria