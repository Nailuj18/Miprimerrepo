def contar_vocales(texto):
    # Definir las vocales (en minúsculas y mayúsculas)
    vocales = "aeiou"
    contador = 0  # Inicializar el contador de vocales

    # Iterar sobre cada carácter del texto
    for letra in texto:
        if letra in vocales:
            contador += 1  # Incrementar el contador si es una vocal

    return contador


# Pedir al usuario que ingrese una palabra o frase
texto_usuario = input("Ingresa una palabra o frase: ")

# Contar las vocales
resultado = contar_vocales(texto_usuario)

# Mostrar el resultado
print(f"La cantidad de vocales es: {resultado}")
