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

def pantalla_inicio():
    pygame.mixer.music.load("Graphics/music_inicio.mp3")
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
                    return
                if exit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(fondo_inicio, (0, 0))
        play_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

def seleccionar_dificultad():
    fondo = pygame.image.load("Graphics/fondoreal.png").convert()
    fondo = pygame.transform.scale(fondo, (WINDOW_WIDTH, WINDOW_HEIGHT))

    font_dif = pygame.font.SysFont(None, 70)

    facil_rect = pygame.Rect(500, 200, 300, 80)
    medio_rect = pygame.Rect(500, 320, 300, 80)
    extremo_rect = pygame.Rect(500, 440, 300, 80)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if facil_rect.collidepoint(event.pos):
                    return "facil"
                if medio_rect.collidepoint(event.pos):
                    return "medio"
                if extremo_rect.collidepoint(event.pos):
                    return "extremo"

        screen.blit(fondo, (0, 0))

       
        pygame.draw.rect(screen, (100, 200, 100), facil_rect)
        pygame.draw.rect(screen, (200, 200, 100), medio_rect)
        pygame.draw.rect(screen, (200, 100, 100), extremo_rect)

       
        screen.blit(font_dif.render("Fácil", True, (0, 0, 0)), (facil_rect.x + 110, facil_rect.y + 15))
        screen.blit(font_dif.render("Medio", True, (0, 0, 0)), (medio_rect.x + 95, medio_rect.y + 15))
        screen.blit(font_dif.render("Extremo", True, (0, 0, 0)), (extremo_rect.x + 70, extremo_rect.y + 15))

        pygame.display.flip()
        clock.tick(FPS)


def elegir_cpu(dificultad, eleccion_jugador):
    if dificultad == "facil":
        return random.choice(["piedra", "papel", "tijeras"])
    elif dificultad == "medio":
        if random.random() < 0.7:
            return gana_a(eleccion_jugador)
        else:
            return random.choice(["piedra", "papel", "tijeras"])
    else:
        return gana_a(eleccion_jugador)

def gana_a(jugador):
    if jugador == "piedra":
        return "papel"
    elif jugador == "papel":
        return "tijeras"
    elif jugador == "tijeras":
        return "piedra"

def jugar(dificultad):
    pygame.mixer.music.load("Graphics/music_juego.mp3")
    pygame.mixer.music.play(-1)

    fondo_juego = pygame.image.load("Graphics/fondoblanco.jpg").convert()
    fondo_juego = pygame.transform.scale(fondo_juego, (WINDOW_WIDTH, WINDOW_HEIGHT))

    corazon_rojo = pygame.transform.scale(pygame.image.load("Graphics/corazonrojo.png").convert_alpha(), (60, 60))
    corazon_azul = pygame.transform.scale(pygame.image.load("Graphics/corazonazul.png").convert_alpha(), (60, 60))

    piedra_img = pygame.transform.scale(pygame.image.load("Graphics/piedra.jpg"), (200, 200))
    papel_img = pygame.transform.scale(pygame.image.load("Graphics/papel.jpg"), (180, 180))
    tijeras_img = pygame.transform.scale(pygame.image.load("Graphics/tijeras.jpg"), (170, 170))

    elecciones = {
        "piedra": piedra_img,
        "papel": papel_img,
        "tijeras": tijeras_img
    }

    vidas_jugador = 3
    vidas_cpu = 3
    eleccion_jugador = None
    eleccion_cpu = None

    font = pygame.font.SysFont(None, 48)

    running = True
    while running:
        screen.blit(fondo_juego, (0, 0))

        
        for i in range(vidas_jugador):
            screen.blit(corazon_rojo, (10 + i * 45, 10))
        for i in range(vidas_cpu):
            screen.blit(corazon_azul, (WINDOW_WIDTH - 12 - (i + 1) * 45, 10))

        screen.blit(piedra_img, (75, 100))
        screen.blit(papel_img, (100, 300))
        screen.blit(tijeras_img, (100, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if pygame.Rect(75, 100, 200, 200).collidepoint(pos):
                    eleccion_jugador = "piedra"
                elif pygame.Rect(100, 300, 180, 180).collidepoint(pos):
                    eleccion_jugador = "papel"
                elif pygame.Rect(100, 500, 170, 170).collidepoint(pos):
                    eleccion_jugador = "tijeras"

                if eleccion_jugador:
                    eleccion_cpu = elegir_cpu(dificultad, eleccion_jugador)

                    screen.blit(elecciones[eleccion_jugador], (500, 250))
                    screen.blit(elecciones[eleccion_cpu], (800, 250))
                    pygame.display.flip()
                    pygame.time.delay(1000)

                    if eleccion_jugador == eleccion_cpu:
                        pass  
                    elif gana_a(eleccion_jugador) == eleccion_cpu:
                        vidas_cpu -= 1
                    else:
                        vidas_jugador -= 1

                    eleccion_jugador = None
                    eleccion_cpu = None

        if vidas_jugador <= 0 or vidas_cpu <= 0:
            running = False

        pygame.display.flip()
        clock.tick(FPS)


    resultado = "¡Ganaste!" if vidas_cpu == 0 else "Perdiste..."
    texto = font.render(resultado, True, (0, 0, 0))
    screen.blit(texto, (WINDOW_WIDTH // 2 - texto.get_width() // 2, 350))
    pygame.display.flip()
    pygame.time.delay(3000)


pantalla_inicio()
dificultad = seleccionar_dificultad()
jugar(dificultad)
 