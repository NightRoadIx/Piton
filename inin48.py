# Módulos a importar
import sys, pygame
from pygame.locals import *
 
# -----------------------------------------------------------------------------
# Constantes
# (TamaÃ±o de la ventana, ancho y alto)
WIDTH = 640
HEIGHT = 480
 
# -----------------------------------------------------------------------------
# Clases

# La clase que genera la bola
class Bola(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        # Llamar al constructor del sprite
        pygame.sprite.Sprite.__init__(self)
        # Cargar la imagen de la pelota
        self.image = load_image("images/ball.png", True)
        # Lo siguiente obtiene el centro de la ventana
        # primero obtiene un rectángulo con las dimensiones
        self.rect = self.image.get_rect()
        # y la posición de la imagen (en este caso el centro)
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        # AquÃ­ se le da la velocidad (en x & en y)
        self.speed = [0.5, -0.5]
        
    # Función para actualizar la posición de la pelota
    # de acuerdo al temporizador (time) y el movimiento de las raquetas-palas
    def actualizar(self, time, pala_jug, pala_cpu, puntos):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
 
        if self.rect.left <= 0:
            puntos[1] += 1
        if self.rect.right >= WIDTH:
            puntos[0] += 1
 
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
            
        # Esto permite conocer si dos objetos colisionaron
        # en este caso la raqueta del jugador con la Bola
        if pygame.sprite.collide_rect(self, pala_jug):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
 
        # Esto permite conocer si dos objetos colisionaron
        # en este caso la raqueta de la computadora con la Bola
        if pygame.sprite.collide_rect(self, pala_cpu):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
 
        return puntos

# La clase para la raqueta/pala
class Pala(pygame.sprite.Sprite):
    # El constructor
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("images/pala.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5
        
    # Función para el movimiento
    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]: # Veriricar que tecl se presiona (arriba)
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]: # (abajo)
                self.rect.centery += self.speed * time
    
    # Esta función es para mover la raqueta del la computadora
    def ia(self, time, ball):
        # Verificiar que la pelota va hacia la raqueta de la computadora
        # pero dando un margen de error, en caso contrario la computadora
        # sería invencíble
        if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:
            # y mover de acuerdo hacia donde va la Bola
            if self.rect.centery < ball.rect.centery:
                self.rect.centery += self.speed * time
            if self.rect.centery > ball.rect.centery:
                self.rect.centery -= self.speed * time

# ---------------------------------------------------------------------
# Funciones

# La función para cargar imágenes
def load_image(filename, transparent=False):
        '''try: image = pygame.image.load(filename)
        except pygame.error, message: pygame.e
                raise SystemExit, message'''
        # Cargar la imagen con el nombre que se le pasa a la función
        image = pygame.image.load(filename)
        # Esto convierte a ujn tipo interno de datos que tiene pygame
        image = image.convert()
        # Esto analaiza si la imagen presenta transperencias (canal alpha)
        if transparent:
                # Con esto obtiene el primer píxel y lo toma como color
                color = image.get_at((0,0))
                ## Este lo define como el color de la transparencia
                image.set_colorkey(color, RLEACCEL)
        return image

# Aquí definimos el texto
def texto(texto, posx, posy, color=(255, 255, 255)):
    # tipo de fuente y tamaño
    fuente = pygame.font.SysFont("comicsansms", 72)
    # convertir la fuente en una imagen para colocar en la ventana
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect 

# ---------------------------------------------------------------------
def main():
    # Colocar el tamaÃ±o de la ventana
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # AquÃ­ se coloca el nombre de la ventana
    pygame.display.set_caption("Pruebas del Pygame")
    
    # Cargar la imagen que estarÃ¡ en el fondo
    background_image = load_image('images/fondo_pong.png')
    # Crear un objeto de la clase Bola()
    bola = Bola()
    # Ahora creamos la raqueta, pala, cesta o como quieran decirle
    # Para el jugador
    pala_jug = Pala(30)
    # y el oponente computadora
    pala_cpu = Pala(WIDTH - 30)
    # Crear un  reloj para el control del tiempo del juego, para poder saber
    # cuanto tiempo ha pasado desde la última actualización ya sea de las
    # raquetas o la bola y poder situarlas en el espacio
    clock = pygame.time.Clock()
    
    # Se inicia el puntaje de ambos jugadores
    puntos = [0, 0]
    
    # Se ejecuta un ciclo infinito
    while True:
        # con esto ahora tenemos el tiempo cada vez que se ejecuta de nuevo el
        # ciclo... el 60 es un parámetro conocido como framerate, lo cual 
        # asegura que el juego no va a más de la velocidad que se coloca
        # no importando si se cambia de computadora 
        time = clock.tick(60)
        # Obtener que tecla es la que se está presionando
        keys = pygame.key.get_pressed()
        
        # Esto proporciona una lista de todos los eventos que esten ocurriendo
        # (presionar teclas, movimiento de objetos, temporizadores)
        for eventos in pygame.event.get():
            # si en algún punto se detecta que se da clic en "X" se cierra
            if eventos.type == QUIT:
                sys.exit(0)
        
        # Analizar cuando se actualiza el estado de la Bola
        puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos)
        # Movimientos de las rawutas/palas del jugador...
        pala_jug.mover(time, keys)
        # y de la computadora
        pala_cpu.ia(time, bola)
 
        p_jug, p_jug_rect = texto(str(puntos[0]), WIDTH/4, 40)
        p_cpu, p_cpu_rect = texto(str(puntos[1]), WIDTH-WIDTH/4, 40)
        
        # Esto coloca la imagen de fondo en la ventana
        # que imagen y en que posición
        screen.blit(background_image, (0, 0))
        # el puntaje jugador
        screen.blit(p_jug, p_jug_rect)
        # el puntajado jugador computadora
        screen.blit(p_cpu, p_cpu_rect)
        # La bola
        screen.blit(bola.image, bola.rect)
        # las raquetas/palas del jugador
        screen.blit(pala_jug.image, pala_jug.rect)
        # las raquetas/palas de la computadora
        screen.blit(pala_cpu.image, pala_cpu.rect)
        # Esto actualiza la ventana
        pygame.display.flip()
    return 0
 
# -----------------------------------------------------------------------------
# Aquí se inicia todo el proceso
if __name__ == '__main__':
    pygame.init()
    main()