import pygame
import time
import random

# Velocidad de la viborita
snake_speed = 15

# Tamaño de la ventana del juego
window_x = 720
window_y = 480

# # # # # # # DEFINICIONES # # # # # # #
# Definir los colores a partir del RGB
# Estos es una tupla de 3 valores RGB de 8 bits
# valores que van de 0 a 255 (2^8 = 256)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)

# Iniciar pygame
pygame.init()

# Iniciar la ventana del juego
pygame.display.set_caption('Nibbles')
# Colocar el tamaño
game_window = pygame.display.set_mode((window_x, window_y))

# Controlador de cuadros por segundo (fps)
fps = pygame.time.Clock()

# Definir la posición inicial de la viborita
snake_position = [100, 50]

# Definir los primeros 4 bloques del cuerpo de la vibora
# (este crecerá)
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Posición de lo que se come la vibora
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
# "Sembrar" lo que come la viborita
fruit_spawn = True

# Colocar la dirección por omisión de la víbora
direction = 'RIGHT'
change_to = direction

# Puntuación inicial
score = 0

def show_score(choice, color, font, size):
    '''
    Función para mostrar la puntuación
    :param choice:
    :param color: color de la fuente
    :param font: tipo de fuente
    :param size: tamaño de la fuente
    :return: None
    '''
    # Crear el objeto fuente con el tipo y tamaño
    score_font = pygame.font.SysFont(font, size)

    # Crear el objeto para el despliegue del sistema
    score_surface = score_font.render('Puntaje : ' + str(score), True, color)

    # Crear un objeto rectangular para el texto
    score_rect = score_surface.get_rect()

    # Desplegar el texto
    game_window.blit(score_surface, score_rect)

def game_over():
    '''
    Función para cuando se termina el juego
    :return:
    '''
    # Crear el objeto para la fuente
    my_font = pygame.font.SysFont('times new roman', 50)

    # Crear una superficie de texto en donde se dibujará el mismo
    game_over_surface = my_font.render(
        'Tu puntaje fue : ' + str(score), True, red)

    # Crear un objeto rectangular para el texto
    game_over_rect = game_over_surface.get_rect()

    # Colocar la posición del texto
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # la función blit dibuja el texto en pantalla
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Tras dos segundos se quita el programa
    time.sleep(2)

    # Apagar pygame
    pygame.quit()

    # se cierra el programa
    quit()

# Ciclo principal
while True:

    # Manejar los eventos del teclado
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Esto es importante, en caso que dos teclas
    # se presionen al mismo tiempo
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Mover a la vibora
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Mecanismo para el crecimiento del cuerpo de la vibora
    # En caso de que, la viborita se coma el cuadro
    # se incrementa por 10 si tamaño
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        # Se desaparece el cuadro de comida de la viborita
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(blue)

    # Dibujar el nuevo tamañao de la vibora
    for pos in snake_body:
        pygame.draw.rect(game_window, yellow,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Condición para que se termine el juego
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Cuando la vibora se toca con las paredes
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Desplegar la puntuación continuamente
    show_score(1, white, 'times new roman', 20)

    # Realizar la actualizació de la pantalla
    pygame.display.update()

    # Cuadros por segundo, velocidad de actualización
    fps.tick(snake_speed)
