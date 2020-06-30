# Import the pygame library
import pygame

# Constants for key presses and actions
from pygame.locals import (
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
COLS = 10
ROWS = 20
BLOCK_WIDTH = SCREEN_WIDTH/COLS
BLOCK_HEIGHT = SCREEN_WIDTH/ROWS

class Stack(pygame.sprite.Sprite):
    def __init__(self, length):
        super(Stack, self).__init__()
        self.surf = pygame.Surface((BLOCK_WIDTH,BLOCK_HEIGHT))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        

# Initialize pygame
pygame.init()

# Sets the size of the window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
stack = Stack(10)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Screen filled with black
    screen.fill((0, 0, 0))

    screen.blit(stack.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    
    pygame.display.flip()