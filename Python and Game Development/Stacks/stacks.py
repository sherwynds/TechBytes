# Get the required library
import pygame

# Game constants
S_WIDTH = 800
S_HEIGHT = 800
COLS = 10
ROWS = 20
B_WIDTH = S_WIDTH/COLS
B_HEIGHT = S_HEIGHT/ROWS
SPEED = 100
COLORS = [(201,44,73), (216,201,155), (216,151,60), (206,113,59), (72,115,132), (15,113,115), (29,47,111), (237,164,189), (44,110,73)]

# Initialize pygame
pygame.init()
# Set up the screen
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Stacks")

# Game variables
<<<<<<< HEAD
left = 0
=======
x = 0
y = S_HEIGHT-B_HEIGHT
>>>>>>> ee1c20d8532b817d7600135b4703557893c29906
width = S_WIDTH
right = left + S_WIDTH
y = S_HEIGHT-B_HEIGHT
directon = 'l'
<<<<<<< HEAD
prev_left = left
prev_right = right
prev_width = width
score = 0
max_score = 0
speed = SPEED
color = COLORS[0]

loop = True
while loop:
    pygame.time.delay(speed)
=======
prev=[x,y,width,height]

loop = True
while loop:
    pygame.time.delay(100)
>>>>>>> ee1c20d8532b817d7600135b4703557893c29906
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
<<<<<<< HEAD
        # If we miss the stack, the game is over
        if right <= prev_left or left >= prev_right:
            pygame.time.delay(1000)
            screen.fill((0,0,0))
            score = 0
            left = 0
            width = S_WIDTH
            right = left + S_WIDTH
            direction = 'l'
            prev_left = left
            prev_right = right
            prev_width = width
            y = S_HEIGHT-B_HEIGHT
            speed = SPEED
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
            color = COLORS[score%9]
            # Move the rectangular block up, and reset the screen if it gets too high
            if y-B_HEIGHT!=B_HEIGHT:
                y -= B_HEIGHT
            else:
                screen.fill((0,0,0))
                pygame.draw.rect(screen, color, (left, S_HEIGHT-B_HEIGHT, prev_width, B_HEIGHT))
                y = S_HEIGHT - 2*B_HEIGHT
                speed = int(speed*0.9)
=======
        prev = [x,y,width,height]
        if x < 0:
            width = width + x
            x = 0
        elif x+width > S_WIDTH:
            width = S_WIDTH - x     
        if y-B_HEIGHT!=B_HEIGHT:
            y -= B_HEIGHT
        else:
            screen.fill((0,0,0))
            pygame.draw.rect(screen, (255,0,0), (prev[0], S_HEIGHT-B_HEIGHT, prev[2], prev[3]))
            y = S_HEIGHT - 2*B_HEIGHT
        
    
>>>>>>> ee1c20d8532b817d7600135b4703557893c29906
    
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