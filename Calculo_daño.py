import math

print("Mata a tu oponente")

while True:
    try:
        arma_aliado = str(
            input("Elije un arma : __MAZO__,__ESPADA___,ARCO__:    "))
        if arma_aliado not in ("MAZO", "ESPADA", "ARCO"):
            print("Elige una de las tres armas anteriores.")
        else:
            break
    except ValueError:
        print("No es valido, elige de nuevo. ")

print("Ahora ataca a tus enemigos:   ")
print("--- : orco")
print("---- : caballero.")
print("---- : elfo oscuro")

while True:
    try:
        enemigo = str(input("A quien quieres matar primero:  ")).lower()
        if enemigo not in ("orco", "caballero", "elfo oscuro"):
            print("Elige a un enemigo.")
        else:
            break
    except ValueError:
        print("Elige a un enemigo")


def calcular_daño(arma, vida_enemigo):
    if arma == "ARCO":
        daño = 15
    elif arma == "MAZA":
        daño = 20
    elif arma == "ESPADA":
        daño = 30
    else:
        daño = 0
    return max(0, vida_enemigo - daño)


vida_enemigo = 100
vida_restante = calcular_daño(arma_aliado, vida_enemigo)
print(f"Usaste {arma_aliado} para atacar al {enemigo}.")
print(f"El daño infligido fue de { vida_restante - vida_enemigo}.")
print(f"La vida restante del {enemigo} es: {vida_restante}.")
