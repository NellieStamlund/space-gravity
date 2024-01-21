import pygame

from Player import Player

def checkEvents():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def clearScreen():
    # Use a color for now
    # TODO: Use a background image instead
    screen.fill("black")


# pygame setup
pygame.init()
screensize = (1280, 720)
screen = pygame.display.set_mode(screensize)

# Global variables
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0.5
objects = []

# player position in pixels
player = Player("Player 1", "red", pygame.Vector2(600,350))


while running:
    checkEvents()
    # Update player from input and gravity
    # Update all other objects from gravity
    clearScreen()
    # Draw all objects

    # Add user input to player velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.thrust(3)
    #if keys[pygame.K_s]:
    if keys[pygame.K_a]:
        player.rotate(-5)
    if keys[pygame.K_d]:
        player.rotate(5)

    # Add gravity
    player.velocity.y += gravity


    player.draw(screen, dt)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()