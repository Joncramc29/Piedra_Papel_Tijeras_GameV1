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

    piedra_img = Button("Graphics/piedra.jpg", (75, 100), scale=0.25) 
    papel_img = Button("Graphics/papel.jpg", (100, 300), scale=0.25)
    tijeras_img = Button("Graphics/tijeras.jpg", (100, 500), scale=0.25)

    piedra_dos = Button("Graphics/piedra2.jpg", (1080, 100) , scale=0.25)
    papel_dos = Button("Graphics/papel2.jpg", (1100, 300), scale=0.25)
    tijeras_dos = Button("Graphics/tijeras2.jpg", (1100, 500), scale=0.25)

    font = pygame.font.SysFont(None, 36)
    resultado = ""

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
        
        piedra_img.draw(screen)
        papel_img.draw(screen)
        tijeras_img.draw(screen)

        piedra_dos.draw(screen)
        papel_dos.draw(screen)
        tijeras_dos.draw(screen)

        if piedra_img.is_pressed():
            resultado_texto = "Elegiste Piedra. " + ganador("piedra", random.choice(["piedra", "papel", "tijeras"]))
        elif papel_img.is_pressed():
            resultado_texto = "Elegiste Papel. " + ganador("papel", random.choice(["piedra", "papel", "tijeras"]))
        elif tijeras_img.is_pressed():
            resultado_texto = "Elegiste Tijeras. " + ganador("tijeras", random.choice(["piedra", "papel", "tijeras"]))

        resultado = font.render(resultado_texto,True, (255, 255, 255))
        screen.blit(resultado_texto, (370, 60))

        pygame.display.flip()
        clock.tick(FPS)

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

def ganador(jugador, cpu):
    if jugador == cpu:
        return f"La cpu eligió {cpu}. ¡Empate!"
    elif (jugador == "piedra" and cpu == "tijeras2") or \
         (jugador == "papel" and cpu == "piedra2") or \
         (jugador == "tijeras" and cpu == "papel2"):
        return f"La cpu eligió {cpu}. ¡Ganaste!"
    else:
        return f"La cpu eligió {cpu}. ¡Perdiste!"

pantalla_inicio()
jugar()