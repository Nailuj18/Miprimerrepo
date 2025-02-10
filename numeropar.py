import math

while True:
    try:
        numero_entero = int(input
                            ("Ingresa un numero:     (0 para salir):   "))
        if numero_entero == 0:
            print("Hasta luego!")
            break
        if numero_entero % 2 == 0:
            print(f"El número {numero_entero} es par.")
        else:

            print(f"El número {numero_entero} es impar.")

    except ValueError:
        print("Ingresa un numero valido.")
    except Exception as e:
        print(f"Se produjo un error: {e}")
