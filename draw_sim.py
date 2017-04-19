import sim
from time import sleep
import pygame
import pygame.gfxdraw
import math

pygame.init()

FONT = pygame.font.SysFont("monospace", 20)

SCREEN_SIZE = 600
SIM_SCALE = SCREEN_SIZE / sim.FIELD_SIZE

SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

CLOCK = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_animal(animal):
    color = WHITE if animal.sex == 'f' else BLACK
    radius = 2 if animal.age < 2 else 4
    x = math.floor(animal.x * SIM_SCALE)
    y = math.floor(animal.y * SIM_SCALE)

    pygame.gfxdraw.filled_circle(SCREEN, x, y, radius, color)
    pygame.gfxdraw.aacircle(SCREEN, x, y, radius, color)

def draw_population_text(animals, year):
    def make_label(color):
        return FONT.render("Population: " + str(len(animals)) + ", Year: " + str(year), 500, color)

    white_label = make_label(WHITE)
    black_label = make_label(BLACK)

    SCREEN.blit(white_label, (8, 8))
    SCREEN.blit(white_label, (10, 8))
    SCREEN.blit(white_label, (12, 8))
    SCREEN.blit(white_label, (8, 10))
    SCREEN.blit(white_label, (12, 10))
    SCREEN.blit(white_label, (8, 12))
    SCREEN.blit(white_label, (10, 12))
    SCREEN.blit(white_label, (12, 12))
    SCREEN.blit(black_label, (10, 10))

def run_and_draw_sim(animals, config):
    running = True
    year = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    animals = sim.step_sim(animals, config)
                    year += 1

        if not running:
            break

        SCREEN.fill(GREEN)

        for animal in animals:
            draw_animal(animal)

        draw_population_text(animals, year)

        pygame.display.flip()

        CLOCK.tick(60)
