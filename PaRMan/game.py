import pygame
from player import Player
from enemies import *
import tkinter
from tkinter import messagebox
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Definir algunos colores como tuplas
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

class Game(object):
    """
    Clase Game
    """
    def __init__(self):
        """
        Constructor de la clase Game
        """
        self.font = pygame.font.Font(None,40)
        self.about = False
        self.game_over = True
        # Crear la variable para la puntuación
        self.score = 0
        # Crear la fuente para desplegar la puntuación en pantalla
        self.font = pygame.font.Font(None,35)
        # Crear el menú para el juego
        self.menu = Menu(("Iniciar","Acerca de","Salir"),font_color = WHITE,font_size=60)
        # Crear el jugador
        self.player = Player(32,128,"player.png")
        # Crear los bloques que generarán los caminos donde se moverá el jugador
        self.horizontal_blocks = pygame.sprite.Group()
        self.vertical_blocks = pygame.sprite.Group()
        # Crear un grupo para los puntos que come Pacman en pantalla
        self.dots_group = pygame.sprite.Group()
        # Colocar el ambiente
        for i,row in enumerate(enviroment()):
            for j,item in enumerate(row):
                if item == 1:
                    self.horizontal_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
                elif item == 2:
                    self.vertical_blocks.add(Block(j*32+8,i*32+8,BLACK,16,16))
        # Crear los enemigos
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Slime(288,96,0,2))
        self.enemies.add(Slime(288,320,0,-2))
        self.enemies.add(Slime(544,128,0,2))
        self.enemies.add(Slime(32,224,0,2))
        self.enemies.add(Slime(160,64,2,0))
        self.enemies.add(Slime(448,64,-2,0))
        self.enemies.add(Slime(640,448,2,0))
        self.enemies.add(Slime(448,320,2,0))
        # Añadir los puntos en el juego
        for i, row in enumerate(enviroment()):
            for j, item in enumerate(row):
                if item != 0:
                    self.dots_group.add(Ellipse(j*32+12,i*32+12,WHITE,8,8))

        # Cargar los efectos de sonido
        self.pacman_sound = pygame.mixer.Sound("pacman_sound.ogg")
        self.game_over_sound = pygame.mixer.Sound("game_over_sound.ogg")


    def process_events(self):
        # Cuando el usuario realiza alguna acción
        for event in pygame.event.get():
            # Si el usuario presiona cerrar
            if event.type == pygame.QUIT:
                return True
            self.menu.event_handler(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.game_over and not self.about:
                        if self.menu.state == 0:
                            # ---- INICIAR ------
                            self.__init__()
                            self.game_over = False
                        elif self.menu.state == 1:
                            # --- ACERCA DE ------
                            self.about = True
                        elif self.menu.state == 2:
                            # --- SALIR -------
                            # El usuario dió clic en la parte de salir
                            return True

                elif event.key == pygame.K_RIGHT:
                    self.player.move_right()

                elif event.key == pygame.K_LEFT:
                    self.player.move_left()

                elif event.key == pygame.K_UP:
                    self.player.move_up()

                elif event.key == pygame.K_DOWN:
                    self.player.move_down()
                
                elif event.key == pygame.K_ESCAPE:
                    self.game_over = True
                    self.about = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.stop_move_right()
                elif event.key == pygame.K_LEFT:
                    self.player.stop_move_left()
                elif event.key == pygame.K_UP:
                    self.player.stop_move_up()
                elif event.key == pygame.K_DOWN:
                    self.player.stop_move_down()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.player.explosion = True
                    
        return False

    def run_logic(self):
        if not self.game_over:
            self.player.update(self.horizontal_blocks,self.vertical_blocks)
            block_hit_list = pygame.sprite.spritecollide(self.player,self.dots_group,True)
            # Cuando block_hit_list contenga un sprite que indique que el jugador dio con un punto
            if len(block_hit_list) > 0:
                # Se aplica el efecto de sonido
                self.pacman_sound.play()
                self.score += 1
            block_hit_list = pygame.sprite.spritecollide(self.player,self.enemies,True)
            if len(block_hit_list) > 0:
                self.player.explosion = True
                self.game_over_sound.play()
            self.game_over = self.player.game_over
            self.enemies.update(self.horizontal_blocks,self.vertical_blocks)
           # tkMessageBox.showinfo("FIN DEL JUEGO!","Puntuación final = "+(str)(GAME.score))

    def display_frame(self,screen):
        # Limpiar la pantalla. No colocar ningún otro comando de dibujo
        screen.fill(BLACK)
        # ---
        if self.game_over:
            if self.about:
                self.display_message(screen,"Es un juego Arcade"+
                "en un laberitno que contiene varios puntos,\n"+
                "conocidos como Pac-Dots, y cuatro fantasmas.\n"+
                "Los cuatro fantasmas recorren el laberinto, intentando atrapar a Pac-Man.\n"+
                "Si uno de ellos lo toca, Pac-Man pierde una vida;\n"+
                "y el juego termina.\n")
            else:
                self.menu.display_frame(screen)
        else:
            # --- Dibujar aquí el juego ---
            self.horizontal_blocks.draw(screen)
            self.vertical_blocks.draw(screen)
            draw_enviroment(screen)
            self.dots_group.draw(screen)
            self.enemies.draw(screen)
            screen.blit(self.player.image,self.player.rect)
            #text=self.font.render("Puntuación: "+(str)(self.score), 1,self.RED)
            #screen.blit(text, (30, 650))
            # Renderizar el texto para el juego
            text = self.font.render("Puntuación: " + str(self.score),True,GREEN)
            # Colocar el texto en pantalla
            screen.blit(text,[120,20])
            
        # --- Continuar y actualizar la pantalla con lo dibujado
        pygame.display.flip()

    def display_message(self,screen,message,color=(255,0,0)):
        label = self.font.render(message,True,color)
        # Obtener el ancho y alto de la etiqueta
        width = label.get_width()
        height = label.get_height()
        # Determinar la posición de la etiqueta
        posX = (SCREEN_WIDTH /2) - (width /2)
        posY = (SCREEN_HEIGHT /2) - (height /2)
        # Dibujar la etiqueta en pantalla
        screen.blit(label,(posX,posY))


class Menu(object):
    """
    Clase Menu
    """
    state = 0
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # Alto total del bloque de texto
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
        
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.state > 0:
                    self.state -= 1
            elif event.key == pygame.K_DOWN:
                if self.state < len(self.items) -1:
                    self.state += 1