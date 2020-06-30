# Get the required library
import pygame

# Game constants
S_WIDTH = 600
S_HEIGHT = 800
COLS = 10
ROWS = 20
B_WIDTH = S_WIDTH/COLS
B_HEIGHT = S_HEIGHT/ROWS
SPEED = 5
# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Stacks")

# Starting stack should be as wide as the screen and as high as a block
x = 0
y = S_HEIGHT-B_HEIGHT
width = S_WIDTH
height = B_HEIGHT
speed = SPEED
directon = 'l'
prev=[]

loop = True
while loop:
    pygame.time.delay(100 )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
   
    # Handle space keypress
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        prev = [x,y,width,height]
        if y-B_HEIGHT!=B_HEIGHT:
            y -= B_HEIGHT
        else:
            screen.fill((0,0,0))
            pygame.draw.rect(screen, (255,0,0), (prev[0], S_HEIGHT-B_HEIGHT, prev[2], prev[3]))
            y = S_HEIGHT - 2*B_HEIGHT
    
    
    # Move the rectangle side to side
    screen.fill((0,0,0), (0,y,S_WIDTH,B_HEIGHT))
    if x < 0-width+2*B_WIDTH:
        directon = 'r'
    elif x > S_WIDTH-2*B_WIDTH:
        directon = 'l'
    if directon == 'r':
        x+=B_WIDTH
    elif directon == 'l':
        x-=B_WIDTH
       

    pygame.draw.rect(screen, (255, 0, 0), (x,y,width,height))

    pygame.display.update()

pygame.quit()
