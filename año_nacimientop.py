while True:
    try:
        año = int(input("Ingresa tu año de nacimiento: "))
        break
    except ValueError:
        print("Por favor ingrese un numero valido.")


edad = (2025 - año)

print(f"Tu edad es {edad}")
print("Gracias por usar nuestros servicios.")
