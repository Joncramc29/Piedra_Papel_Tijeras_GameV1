import pygame
import sys
import random
 
pygame.init()
 
DIMENSIONS = (1376, 768)
screen = pygame.display.set_mode((DIMENSIONS))
pygame.display.set_caption("Juego de Piedra, Papel o Tijera")
 
clock = pygame.time.Clock()
FPS = 60
 
def pantalla_inicio():
    pygame.mixer.music.load("Graphics/music_inicio.mp3")
    pygame.mixer.music.play(-1)
    
    fondo_inicio = pygame.image.load("Graphics/fondoreal.png").convert()
    fondo_inicio = pygame.transform.scale(fondo_inicio, (DIMENSIONS))
 
    play_button = Button("Graphics/play.png", (530, 215), scale=0.2)
    exit_button = Button("Graphics/exit1.png", (530, 350), scale=0.2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
        if play_button.is_pressed():
            return  
 
        if exit_button.is_pressed():
            pygame.quit()
            sys.exit()

        screen.blit(fondo_inicio, (0, 0))
        play_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

def jugar():

    fondo_juego = pygame.image.load("Graphics/fondo_juego.png").convert()
    fondo_juego = pygame.transform.scale(fondo_juego, DIMENSIONS)

    piedra_btn = Button("Graphics/piedra.jpg", (100, 400), scale=0.5)
    papel_btn = Button("Graphics/papel.jpg", (400, 420), scale=0.4)
    tijeras_btn = Button("Graphics/tijeras.jpg", (700, 400), scale=0.35)

    font = pygame.font.SysFont(None, 36)
    resultado_texto = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(fondo_juego, (0, 0))

        piedra_btn.draw(screen)
        papel_btn.draw(screen)
        tijeras_btn.draw(screen)

        if piedra_btn.is_pressed():
            resultado_texto = "Elegiste Piedra. " + ganador("piedra", random.choice(["piedra", "papel", "tijeras"]))
        elif papel_btn.is_pressed():
            resultado_texto = "Elegiste Papel. " + ganador("papel", random.choice(["piedra", "papel", "tijeras"]))
        elif tijeras_btn.is_pressed():
            resultado_texto = "Elegiste Tijeras. " + ganador("tijeras", random.choice(["piedra", "papel", "tijeras"]))

        texto_render = font.render(resultado_texto, True, (255, 255, 255))
        screen.blit(texto_render, (100, 300))

        pygame.display.flip()
        clock.tick(FPS)

class Button:
    def __init__(self, image_path, position, scale=0.2):
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

def ganador(jugador, computadora):
    if jugador == computadora:
        return f"La computadora eligió {computadora}. ¡Empate!"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        return f"La computadora eligió {computadora}. ¡Ganaste!"
    else:
        return f"La computadora eligió {computadora}. ¡Perdiste!"

pantalla_inicio()
jugar()
