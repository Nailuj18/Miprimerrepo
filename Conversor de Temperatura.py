import math

while True:
    try:
        temperatura = int(input("Ingrese la temperatura en Celcius °:  "))

    except ValueError:
        print("Ingresa un numero valido.")
    break

Fahrenheit = ((temperatura*9/5 + 32))

print(f"La temperatura en fahrenheit es: {Fahrenheit}")
