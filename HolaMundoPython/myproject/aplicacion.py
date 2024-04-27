


peso = int(input( "Ingrese su peso"))
altura = float(input("Ingrese su altura en mts"))

imc = round(peso/(altura**2),2)

print(f"Su imc es: {imc}")

caso1 = "bajo peso"
caso2 = "peso normal"
caso3 = "sobre peso"
caso4 = "Obesidad"

if imc< 18.5:
    print(caso1)
elif imc >= 18.5 and  imc < 25:
    print(caso2)
elif imc >= 25 and imc < 30 :
    print(caso3)
else:
    print(caso4)
