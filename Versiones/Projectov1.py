import pygame
import sys
import random

pygame.init()


WINDOW_WIDTH = 1376
WINDOW_HEIGHT = 768
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Juego de Piedra, Papel o Tijera")

clock = pygame.time.Clock()
FPS = 60


class Button:
    def __init__(self, image_path, position, scale=1.0):
        self.image = pygame.image.load(image_path).convert_alpha()
        width = int(self.image.get_width() * scale)
        height = int(self.image.get_height() * scale)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        return self.rect.collidepoint(mouse_pos) and mouse_click

def pantalla_inicio():
    pygame.mixer.music.load("Graphics/music_juego.mp3")
    pygame.mixer.music.play(-1)

    fondo_inicio = pygame.image.load("Graphics/fondoreal.png").convert()
    fondo_inicio = pygame.transform.scale(fondo_inicio, (WINDOW_WIDTH, WINDOW_HEIGHT))

    play_button = Button("Graphics/play.png", (530, 215), scale=0.2)
    exit_button = Button("Graphics/exit1.png", (530, 415), scale=0.2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(event.pos):
                    return  # Sale del menú e inicia el juego
                if exit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(fondo_inicio, (0, 0))
        play_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

      

def jugar():
    pygame.mixer.music.load("Graphics/music_juego.mp3")
    pygame.mixer.music.play(-1)

    fondo_juego = pygame.image.load("Graphics/fondoblanco.jpg").convert()
    fondo_juego = pygame.transform.scale(fondo_juego, (WINDOW_WIDTH, WINDOW_HEIGHT))

    corazon_rojo = pygame.image.load("Graphics/corazonrojo.png").convert_alpha()
    corazon_azul = pygame.image.load("Graphics/corazonazul.png").convert_alpha()
    corazon_rojo = pygame.transform.scale(corazon_rojo, (60, 60))
    corazon_azul = pygame.transform.scale(corazon_azul, (60, 60))

    vidas_jugador = 3
    vidas_cpu = 3

    piedra_img = pygame.image.load("Graphics/piedra.jpg")
    papel_img = pygame.image.load("Graphics/papel.jpg")
    tijeras_img = pygame.image.load("Graphics/tijeras.jpg")

    piedra_img = pygame.transform.scale(piedra_img, (200, 200))
    papel_img = pygame.transform.scale(papel_img, (180, 180))
    tijeras_img = pygame.transform.scale(tijeras_img, (170, 170))

    piedra_dos = pygame.image.load("Graphics/piedra2.jpg")
    papel_dos = pygame.image.load("Graphics/papel2.jpg")
    tijeras_dos = pygame.image.load("Graphics/tijeras2.jpg")

    piedra_dos = pygame.transform.scale(piedra_dos, (200, 200))
    papel_dos = pygame.transform.scale(papel_dos, (180, 180))
    tijeras_dos = pygame.transform.scale(tijeras_dos, (170, 170))

    font = pygame.font.SysFont(None, 36)
    resultado_texto = ""

    puntos_jugador = 0
    puntos_ordenador = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.blit(fondo_juego, (0, 0))

        
        for i in range(vidas_jugador):
            screen.blit(corazon_rojo, (10 + i * 45, 10))

        
        for i in range(vidas_cpu):
            screen.blit(corazon_azul, (WINDOW_WIDTH - 12 - (i + 1) * 45, 10))

        
        screen.blit(piedra_img, (75, 100))
        screen.blit(papel_img, (100, 300))
        screen.blit(tijeras_img, (100, 500))

        
        screen.blit(piedra_dos, (1080, 100))
        screen.blit(papel_dos, (1100, 300))
        screen.blit(tijeras_dos, (1100, 500))



        texto_render = font.render(resultado_texto, True, (255, 255, 255))
        screen.blit(texto_render, (100, 300))

        pygame.display.flip()
        clock.tick(FPS)

def ganador(jugador, computadora):
    if jugador == computadora:
        return f"La computadora eligió {computadora}. ¡Empate!"
    elif (jugador == "piedra" and computadora == "tijeras2") or \
         (jugador == "papel" and computadora == "piedra2") or \
         (jugador == "tijeras" and computadora == "papel2"):
        return f"La computadora eligió {computadora}. ¡Ganaste!"
    else:
        return f"La computadora eligió {computadora}. ¡Perdiste!"

pantalla_inicio()
jugar()