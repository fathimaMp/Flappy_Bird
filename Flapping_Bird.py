import pygame
import sys
import random

# Initialize pygame 
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600 
SCREEN_HEIGHT = 500
FPS = 50

# Colors
BACKGROUND_COLOR = (606060)  
GROUND_COLOR = (139, 69, 19)        
BIRD_COLOR = (255, 223, 0)          
PIPE_COLOR = (34, 139, 34)          
TEXT_COLOR = (255, 255, 255)        

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Bird settings
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
bird = pygame.Rect(200, 250, BIRD_WIDTH, BIRD_HEIGHT)

# Pipe settings
PIPE_WIDTH = 50  
PIPE_GAP = 150
pipes = []
pipe_timer = 0

# Gravity and speed
gravity = 0.25
bird_velocity = 0
pipe_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Functions
def draw_bird():
    pygame.draw.ellipse(screen, BIRD_COLOR, bird)

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, PIPE_COLOR, pipe)

def move_pipes():
    for pipe in pipes:
        pipe.x -= pipe_speed
    if pipes and pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.pop(0) 
        global score
        score += 1

def check_collision():
    for pipe in pipes:
        if bird.colliderect(pipe):
            return True
    if bird.top < 0 or bird.bottom > SCREEN_HEIGHT:
        return True
    return False

def display_score():
    text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = -6  

    # Bird mechanics
    bird_velocity += gravity
    bird.y += bird_velocity

    # Pipe mechanics
    pipe_timer += 1
    if pipe_timer > 90:
        pipe_timer = 0
        pipe_x = SCREEN_WIDTH
        pipe_y = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        pipes.append(pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_y))  
        pipes.append(pygame.Rect(pipe_x, pipe_y + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_y - PIPE_GAP))  

    move_pipes()
    draw_pipes()
    draw_bird()

    # Collision check
    if check_collision():
        running = False

    display_score()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
