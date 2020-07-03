# Get the required library
import pygame

# Game constants
S_WIDTH = 800               # Screen width and height
S_HEIGHT = 800
COLS = 10                   # Number of columns and rows
ROWS = 20
B_WIDTH = S_WIDTH/COLS      # Block width and height
B_HEIGHT = S_HEIGHT/ROWS
SPEED = 100                 # Initial speed
COLORS = [(213,62,79),(244,109,67),(253,174,97),(254,224,139),(255,255,191),(230,245,152),(171,221,164),(102,194,165),(50,136,189),(102,194,165),(171,221,164),(230,245,152),(255,255,191),(254,224,139),(253,174,97),(244,109,67)]

# Initialize pygame
pygame.init()
# Set up the screen
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Stacks")

# Game variables
left = 0
width = S_WIDTH
right = left + S_WIDTH
prev_left = left
prev_right = right
prev_width = width
y = S_HEIGHT-B_HEIGHT
directon = 'l'
score = 0
max_score = 0
speed = SPEED
color = COLORS[0]

loop = True
while loop:
    pygame.time.delay(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # On each tick, render the score and the max score to the screen
    screen.fill((0,0,0), (0,0,S_WIDTH,B_HEIGHT))
    font = pygame.font.SysFont('comicsans', 30)
    text = font.render("Score: " + str(score) + "     Max: " + str(max_score), 1, (255,255,255))
    screen.blit(text, (S_WIDTH/2-100, 2))

    # Handle space keypress:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # If we miss the stack, the game is over
        if right <= prev_left or left >= prev_right:
            pygame.time.delay(1000)
            screen.fill((0,0,0))
            score = 0
            left = 0
            width = S_WIDTH
            right = left + S_WIDTH
            prev_left = left
            prev_right = right
            prev_width = width
            y = S_HEIGHT-B_HEIGHT
            direction = 'l'
            speed = SPEED
            color = COLORS[0]
        # Otherwise
        else:
            # Cut the block off if it misses the edge of the stack
            if left != prev_left:
                left = max(left, prev_left)
                right = min(right, prev_right)
                width = right-left
            # Increment the score
            score += 1
            max_score = max(score,max_score)
            # Save the current coordinates as the previous
            prev_left = left
            prev_right = right
            prev_width = width
            # Draw the placed rectangle to the screen
            screen.fill((0,0,0), (0,y,S_WIDTH,B_HEIGHT))
            pygame.draw.rect(screen, color, (left,y,width,B_HEIGHT))
            # Move the rectangular block up, and reset the screen if it gets too high
            if y-B_HEIGHT!=B_HEIGHT:
                y -= B_HEIGHT
                color = COLORS[score%16]
            else:
                screen.fill((0,0,0))
                pygame.draw.rect(screen, color, (left, S_HEIGHT-B_HEIGHT, prev_width, B_HEIGHT))
                color = COLORS[score%16]
                y = S_HEIGHT - 2*B_HEIGHT
                speed = int(speed*0.97)
    
    # Move the rectangle side to side
    screen.fill((0,0,0), (0,y,S_WIDTH,B_HEIGHT))
    if left < 0-width+2*B_WIDTH:
        directon = 'r'
    elif left > S_WIDTH-2*B_WIDTH:
        directon = 'l'
    if directon == 'r':
        left+=B_WIDTH
        right+=B_WIDTH
    elif directon == 'l':
        left-=B_WIDTH
        right-=B_WIDTH
    pygame.draw.rect(screen, color, (left,y,width,B_HEIGHT))

    pygame.display.update()

pygame.quit()