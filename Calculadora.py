import os
while True:

    valor1 = int(input("Ingresa el primer digito: "))
    valor2 = int(input("Ingresa el segundo digito: "))

    try:
        operacion = (
            input("elige una operacion : (+ , - , / , * .):  ")).strip()

        if operacion == "+":
            resultado = valor1 + valor2
            print(f"{valor1} + {valor2} = {resultado}")

        elif operacion == "-":
            resultado = valor1 - valor2
            print(f"{valor1} - {valor2} = {resultado}")

        elif operacion == "/":
            if valor2 == 0:
                print("No se puede dividir por 0")

            else:
                resultado = valor1 / valor2
                print(f"{valor1} / {valor2} = {resultado}")

        elif operacion == "*":
            resultado = valor1 * valor2
            print(f"{valor1} * {valor2} = {resultado}")

        else:
            print("Ingresa una operacion valida. ")
            continue

        otra_operacion = input(
            "¿Quieres hacer otra operación? (si/no): ").lower()

        if otra_operacion != "si":
            print("Hasta pronto")
        except ValueError:
        print("Ingresa otro digito")
        break
