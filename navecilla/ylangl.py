import pygame
import random

# Importar pygame.locals para un acceso más sencillo a las
# teclas y coordenadas.
# Actualizado conforme a estándares plafe8 y black
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Definir las constantes para el ancho y alto de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    """
    Define la clase Player que extiende pygame.sprite.Sprite (hereda sus características)
    La superficie que se dibuja en pantalla es ahora una propiedad del mismo jugador
    """
    def __init__(self):
        """
            Constructor de la clase Player()
            Inicia ciertas propiedades del fondo
        """
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # Move the sprite based on keypresses
    def update(self, pressed_keys):
        """
        Para actualizar la posición del sprite
        basado en lo que se presionó de tecla
        :param pressed_keys:
        :return: None
        """
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Mantener al jugador en pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    """
    Define la clase Enemy que al igual que Player, extiene o hereda de
    pygame.sprite.Sprite
    """
    def __init__(self):

        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((20, 10))
        #self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        """
        Mover el sprite basado en la velocidad
        Removerlo cuando pase por el borde izquierdo
        de la pantalla
        :return: None
        """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    """
    Definir el objeto Cloud heredando de pygame.sprite.Sprite
    Se usa una imagen para que se vea más mejor
    """
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # La posición inicial es generada de manera aleatoria
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Mover la nube basado en una velocidad constante
    # Remover la nube cuando pase por la parte izquierda de la ventana
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

# Configurar el reloj para una tasa de actualización decente
clock = pygame.time.Clock()

# Iniciar pygame
pygame.init()

# Crear el objeto ventana, cuyo tamaño está determinado por:
# SCREEN_WIDTH y SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Crear un evento personalizado para añadir un nuevo enemigo
ADDENEMY = pygame.USEREVENT + 1
# Esto se hará cada 1000 ms
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Crear al jugador
player = Player()

# Crear grupos para mantener los sprites de los enemigos
# y cada sprite
# - enemies es utilizado para la detección de la colisión y actualización de posición
# - clouds es utilizado para la actualización de las nubes
# - all_sprites es usado para renderizar
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable para mantener el juego activo
running = True

# Ciclo
while running:
    # Ver en cada evento en la fila
    for event in pygame.event.get():
        # Si el usuario presionó una tecla
        if event.type == KEYDOWN:
            # En caso de la tecla ESC
            if event.key == K_ESCAPE:
                running = False

        # El usuario presionó el botón de cierre 'x'
        elif event.type == QUIT:
            running = False

        # Debe añadirse un nuevo enemigo
        elif event.type == ADDENEMY:
            # Crear un nuevo enemigo y añadirlo al grupo de sprites
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Añadir una nueva nube
        elif event.type == ADDCLOUD:
            # Crear una nueva nube y añadirlo al grupo de sprites
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # Obtener el conjunto de teclas y verificar la entrada del usuario
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Actualizar la posición del enemigo
    enemies.update()
    clouds.update()

    # Rellenar la pantalla con color negro
    screen.fill((135, 206, 250))

    # Dibujar todos los sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Revisar si algún enemigo ha colisionado con el jugador
    if pygame.sprite.spritecollideany(player, enemies):
        # Si es el caso, remover al jugador y detener el ciclo
        player.kill()
        running = False

    # Voltea la pantalla para desplegar
    pygame.display.flip()

    # Asegurar que el programa mantenga 30 fps
    clock.tick(30)
