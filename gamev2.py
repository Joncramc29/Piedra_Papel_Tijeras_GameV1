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

    font_dif = pygame.font.Font("Graphics/pixel_font.ttf", 35)

    facil_rect = pygame.Rect(540, 300, 300, 80)
    medio_rect = pygame.Rect(540, 400, 300, 80)
    extremo_rect = pygame.Rect(540, 500, 300, 80)

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

        texto_facil = font_dif.render("Fácil", True, (0, 0, 0))
        texto_medio = font_dif.render("Medio", True, (0, 0, 0))
        texto_extremo = font_dif.render("Extremo", True, (0, 0, 0))

        screen.blit(texto_facil, texto_facil.get_rect(center=facil_rect.center))
        screen.blit(texto_medio, texto_medio.get_rect(center=medio_rect.center))
        screen.blit(texto_extremo, texto_extremo.get_rect(center=extremo_rect.center))

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
        return "tijeras"
    elif jugador == "papel":
        return "piedra"
    elif jugador == "tijeras":
        return "papel"

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

    piedra_dos = pygame.transform.scale(pygame.image.load("Graphics/piedra2.jpg"), (200, 200))
    papel_dos = pygame.transform.scale(pygame.image.load("Graphics/papel2.jpg"), (180, 180))
    tijeras_dos = pygame.transform.scale(pygame.image.load("Graphics/tijeras2.jpg"), (170, 170))

    elecciones = {
        "piedra": piedra_img,
        "papel": papel_img,
        "tijeras": tijeras_img
    }

    elecciones_dos = {
        "piedra": piedra_dos,
        "papel": papel_dos,
        "tijeras": tijeras_dos
    }

    vidas_jugador = 3
    vidas_cpu = 3
    eleccion_jugador = None
    eleccion_cpu = None

    font = pygame.font.Font("Graphics/pixel_font.ttf", 48)

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

        screen.blit(piedra_dos, (1080, 100))
        screen.blit(papel_dos, (1100, 300))
        screen.blit(tijeras_dos, (1100, 500))

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

                    img_jugador = elecciones[eleccion_jugador]
                    img_cpu = elecciones_dos[eleccion_cpu]

                    x_jugador = WINDOW_WIDTH // 2 - img_jugador.get_width() - 20
                    x_cpu = WINDOW_WIDTH // 2 + 20
                    y = WINDOW_HEIGHT // 2 - img_jugador.get_height() // 2

                    screen.blit(img_jugador, (x_jugador, y))
                    screen.blit(img_cpu, (x_cpu, y))
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