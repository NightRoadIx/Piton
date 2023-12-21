import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

# Definir algunos colores
BLACK = (0,0,0)
WHITE = (255,255,255)

class Player(pygame.sprite.Sprite):
    """
    Clase Player, hereda de la clase pygame.sprite.Sprite
    """
    change_x = 0
    change_y = 0
    explosion = False
    game_over = False
    def __init__(self,x,y,filename):
        # Llamar al constructor de la clase padre (sprite)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        # Cargar la imagen que se usará para la animación
        img = pygame.image.load("walk.png").convert()
        # Crear los objetos para la animación
        self.move_right_animation = Animation(img,32,32)
        self.move_left_animation = Animation(pygame.transform.flip(img,True,False),32,32)
        self.move_up_animation = Animation(pygame.transform.rotate(img,90),32,32)
        self.move_down_animation = Animation(pygame.transform.rotate(img,270),32,32)
        # Cargar la imagen de la explosión
        img = pygame.image.load("explosion.png").convert()
        self.explosion_animation = Animation(img,30,30)
        # Salvar la imagen del jugador
        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)

    def update(self,horizontal_blocks,vertical_blocks):
        if not self.explosion:
            if self.rect.right < 0:
                self.rect.left = SCREEN_WIDTH
            elif self.rect.left > SCREEN_WIDTH:
                self.rect.right = 0
            if self.rect.bottom < 0:
                self.rect.top = SCREEN_HEIGHT
            elif self.rect.top > SCREEN_HEIGHT:
                self.rect.bottom = 0
            self.rect.x += self.change_x
            self.rect.y += self.change_y

            # Esto detiene al usuario de que se mueva hacia arriba o abajo
            # dentro de la caja

            for block in pygame.sprite.spritecollide(self,horizontal_blocks,False):
                self.rect.centery = block.rect.centery
                self.change_y = 0
            for block in pygame.sprite.spritecollide(self,vertical_blocks,False):
                self.rect.centerx = block.rect.centerx
                self.change_x = 0

            # Esto hace que la animación inicie
            
            if self.change_x > 0:
                self.move_right_animation.update(10)
                self.image = self.move_right_animation.get_current_image()
            elif self.change_x < 0:
                self.move_left_animation.update(10)
                self.image = self.move_left_animation.get_current_image()

            if self.change_y > 0:
                self.move_down_animation.update(10)
                self.image = self.move_down_animation.get_current_image()
            elif self.change_y < 0:
                self.move_up_animation.update(10)
                self.image = self.move_up_animation.get_current_image()
        else:
            if self.explosion_animation.index == self.explosion_animation.get_length() -1:
                pygame.time.wait(500)
                self.game_over = True
            self.explosion_animation.update(12)
            self.image = self.explosion_animation.get_current_image()
            

    def move_right(self):
        self.change_x = 3

    def move_left(self):
        self.change_x = -3

    def move_up(self):
        self.change_y = -3

    def move_down(self):
        self.change_y = 3

    def stop_move_right(self):
        if self.change_x != 0:
            self.image = self.player_image
        self.change_x = 0

    def stop_move_left(self):
        if self.change_x != 0:
            self.image = pygame.transform.flip(self.player_image,True,False)
        self.change_x = 0

    def stop_move_up(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image,90)
        self.change_y = 0

    def stop_move_down(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image,270)
        self.change_y = 0



class Animation(object):
    def __init__(self,img,width,height):
        # Cargar la hoja del sprite
        self.sprite_sheet = img
        # Crear la lista para almacenar las imágenes
        self.image_list = []
        self.load_images(width,height)
        # Crear una variable la cual mantendrá la imagen actual en la lista
        self.index = 0
        # Crear una variable que mantendrá el tiempo
        self.clock = 1
        
    def load_images(self,width,height):
        # Recorrer a través de cada imagen de la hoja del sprite
        for y in range(0,self.sprite_sheet.get_height(),height):
            for x in range(0,self.sprite_sheet.get_width(),width):
                # Cargar la imagen en una lista
                img = self.get_image(x,y,width,height)
                self.image_list.append(img)

    def get_image(self,x,y,width,height):
        # Crear una nueva imagen en blanco
        image = pygame.Surface([width,height]).convert()
        # Copiar el sprite de la hoja grande en la pequeña
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        # Asumir que el color negro actua como transparente
        image.set_colorkey((0,0,0))
        # Regresar la imagen
        return image

    def get_current_image(self):
        return self.image_list[self.index]

    def get_length(self):
        return len(self.image_list)

    def update(self,fps=30):
        step = 30 // fps
        l = range(1,30,step)
        if self.clock == 30:
            self.clock = 1
        else:
            self.clock += 1

        if self.clock in l:
            # Incrementar el índice
            self.index += 1
            if self.index == len(self.image_list):
                self.index = 0