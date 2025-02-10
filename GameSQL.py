import psycopg2
import pygame

try:
    # Conexión a la base de datos en SQL
    conn = psycopg2.connect(user='postgres',
                            password='123456789',
                            host='localhost',
                            port='5432',
                            database='empresa')
    cursor = conn.cursor()

    # Crear la tabla de puntuaciones si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS puntuaciones (
        id SERIAL PRIMARY KEY,
        jugador_nombre VARCHAR(100),
        puntuacion INT
    );
    """)
    conn.commit()

    # Inicializar Pygame
    pygame.init()

    # Configuración del juego
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de Disparos")
    reloj = pygame.time.Clock()

    # Variables del juego
    jugador_nombre = "Jugador1"
    puntuacion = 0

    # Bucle principal del juego
    corriendo = True
    while corriendo:
        pantalla.fill((0, 0, 0))  # Fondo negro

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Lógica del juego (ejemplo básico de aumento de puntuación)
        puntuacion += 1

        # Mostrar puntuación en la pantalla
        fuente = pygame.font.SysFont('Arial', 36)
        texto = fuente.render(
            f"Puntuación mis perros: {puntuacion}", True, (255, 255, 255))
        pantalla.blit(texto, (10, 10))

        pygame.display.flip()
        reloj.tick(50)  # 30 FPS

    # Después de terminar el juego, verificar y guardar la puntuación
    cursor.execute("""
    SELECT MAX(puntuacion) FROM puntuaciones WHERE jugador_nombre = %s;
    """, (jugador_nombre,))
    resultado = cursor.fetchone()

    # Si el jugador tiene puntuaciones previas, solo guardar la nueva si es mayor
    puntuacion_maxima = resultado[0] if resultado[0] is not None else 0

    if puntuacion > puntuacion_maxima:
        cursor.execute("""
        INSERT INTO puntuaciones (jugador_nombre, puntuacion)
        VALUES (%s, %s)
        """, (jugador_nombre, puntuacion))
        conn.commit()
        print(f"Nuevo récord: {puntuacion}")

    else:
        print(f"Puntuación guardada: {puntuacion}")

    # Cerrar la conexión
    cursor.close()
    conn.close()

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Salir del juego
    pygame.quit()
