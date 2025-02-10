# Importar la librería psycopg2
import psycopg2

try:
    # Conexión a la base de datos en SQL
    conn = psycopg2.connect(user='postgres',
                            password='123456789',
                            host='localhost',
                            port='5432',
                            database='empresa')

    print("Conexión exitosa")

    # Crear un cursor
    cursor = conn.cursor()
# Ejecutar la consulta SELECT
    cursor.execute("""SELECT * FROM empleados""")

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    # Imprimir los resultados
    if resultados:
        for row in resultados:
            print(row)  # Imprime cada fila de los resultados
    else:
        print("No hay empleados en la base de datos.")

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Ocurrió un error: {e}")
