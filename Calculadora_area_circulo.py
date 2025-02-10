import math

print("Vamos a hallar el area del circulo.")

while True:
    try:
        radio = int(input("Por favor ingresa el radio del circulo"))
        if radio <= 0:
            print("El radio debe ser un numero positivo.")
        else:
            break
    except ValueError:
        print("Ingresa un numero valido.")

area = (math.pi * (radio)**2)

print(f"El Area del ciruclo es :{area.}").f2
