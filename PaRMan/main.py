import pygame
from game import Game

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576

def main():
    # Iniciar pygame
    pygame.init()
    # Colocar las características de la pantalla en [ancho, alto]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Colocar el título de la ventana
    pygame.display.set_caption("PACMAN")
    # Para el ciclo infinito
    done = False
    # Con esto se manejan las actualizaciones de la pantalla
    clock = pygame.time.Clock()
    # Crear un objeto de juego
    game = Game()

    # CICLO INFINITO
    while not done:
        # Eventos del proceso (teclado, clic del ratón, etc)
        done = game.process_events()
        # Lógica del juego
        game.run_logic()
        # Dibujar el frame actual
        game.display_frame(screen)
        # Limitar a 30 cuadros por segundo
        clock.tick(30)
        # tkMessageBox.showinfo("GAME OVER!","Puntuación final = "+(str)(GAME.score))
    # Una vez que se salga del juego
    pygame.quit()

if __name__ == '__main__':
    # Ejecutar el principal del juego
    main()
