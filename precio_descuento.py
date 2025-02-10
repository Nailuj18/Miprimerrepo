import math

while True:
    try:
        precio_original = float(input("Ingresa el precio original: "))
        if precio_original <= 0:
            print("Ingresa un numero positivo")
        else:
            break
    except ValueError:
        print("Ingrese un numero valido.")
while True:
    try:
        descuento = int(
            input("Ingresa el porcentaje de descuento que se aplicará."))
        if descuento <= 0:
            print("Ingresa un numero positivo")
        else:
            break
    except ValueError:
        print("Ingrese un numero valido.")

descuento_final = precio_original * (descuento/100)
precio_final = precio_original - descuento_final

print(f"Tu descuento será del: {descuento} %")
print(f"Tu descuento es de: {descuento_final:.2f}")
print(f"Precio final de: {precio_final:.2f}")
