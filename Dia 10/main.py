import pygame
import random
import math
from pygame import mixer


# Inicializar Pygame
pygame.init()

# Crear una ventana
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invación espacial")
icono = pygame.image.load("img/ovni.png")
fondo = pygame.image.load("img/fondo.jpg")
pygame.display.set_icon(icono)

#agregar música
mixer.music.load("sound/MusicaFondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)


valor_movimiento = 0.3

#variables del jugador
img_jugador = pygame.image.load("img/cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

#crear enemigos
for i in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("img/enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(valor_movimiento)
    enemigo_y_cambio.append(50)

#variables de la bala
balas = []
img_bala = pygame.image.load("img/bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Game Over Texto
fuente_game_over = pygame.font.Font('freesansbold.ttf', 64)

# Función para mostrar el texto de Game Over
def texto_game_over():
    game_over_texto = fuente_game_over.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(game_over_texto, (200, 250))


# Función para mostrar el puntaje
def mostrar_puntaje(x, y):
    puntaje_texto = fuente.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
    pantalla.blit(puntaje_texto, (x, y))

# Función para mostrar al jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Función para mostrar al jugador
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# función declarar colisión
def colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distancia < 27:
        return True
    else:
        return False

# Bucle principal
se_ejecuta = True
while se_ejecuta:

    #imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # ieración de eventos
    for event in pygame.event.get():
        # Salir del juego
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jugador_x_cambio -= 1
            if event.key == pygame.K_RIGHT:
                jugador_x_cambio += 1

            if event.key == pygame.K_SPACE:
                mixer.Sound("sound/disparo.mp3").play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                    }
                balas.append(nueva_bala)


        # Detener el movimiento del jugador
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio

    # Limitar el movimiento del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Actualizar la posición del enemigo
    for i in range(cantidad_enemigos):

        # Game Over
        if enemigo_y[i] > 500:
            for j in range(cantidad_enemigos):
                enemigo_y[j] = 2000
            texto_game_over()
            balas.clear()
            break


        enemigo_x[i] += enemigo_x_cambio[i]

        # Limitar el movimiento del enemigo
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = valor_movimiento
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -valor_movimiento
            enemigo_y[i] += enemigo_y_cambio[i]

        # Colisión
        for bala in balas:
            colision_enemigo = colision(enemigo_x[i], enemigo_y[i], bala["x"], bala["y"])
            if colision_enemigo:
                mixer.Sound("sound/golpe.mp3").play()
                bala["y"] = 500
                bala_visible = False
                puntaje += 1

                enemigo_x[i] = random.randint(0, 736)
                enemigo_y[i] = random.randint(50, 200)
                break

        enemigo(enemigo_x[i], enemigo_y[i],i)

    # mover la bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    '''if bala_y <= -64:
        bala_y = 500
        bala_visble = False'''


    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
        # Limitar el movimiento de la bala
        '''
        if bala_y <= 0:
            bala_visble = False
            bala_y = 500
        '''

    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    # Actualizar la pantalla
    pygame.display.update()
