import pyodbc
from datetime import datetime

# CONECTANDO A LA BASDE DE DATOS SQL SERVER
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=servidorjulianazure.database.windows.net;'
                      'DATABASE=Basenueva;'
                      'UID=cloudadmin;'
                      'PWD=Ju917342685.'
                      )

conn = conn.cursor()


def obtener_fecha_lanzamiento():
    while True:
        fecha_lanzamiento = input(
            "Ingresa la fecha de lanzamiento del juego (YYYY-MM-DD):  ")
        try:
            datetime.strptime(fecha_lanzamiento, "%Y-%m-%d")
            return fecha_lanzamiento
        except ValueError:
            print("Fecha invalida, Por favor ingrese el siguiente formato (YYYY-MM-DD)")


# CREAR UNA FUNCION PARA SOLICTAR AL USUARIO EL JUEGO
def datos_del_juego():

    nombre = input("Nombre del juego: ")
    categoria = input("Categoria del juego: ")
    editor = input("Editor del juego: ")
    fecha_lanzamiento = obtener_fecha_lanzamiento()

    return (nombre, categoria, editor, fecha_lanzamiento)


juego = datos_del_juego()
print(juego)


def insertar_juego(cursor, juego):
     cursor.execute("""
        INSERT INTO Juegos (nombre, categoria, desarrollado, fecha_lanzamiento)
        VALUES (?, ?, ?, ?)
    """, juego)

    cursor.commit()
    
    
