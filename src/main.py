import pygame

from Player import Player

def getPolygon(position):
    return [(position.x+10,position.y), (position.x,position.y+25), (position.x+10,position.y+20), (position.x+20,position.y+25)]

def checkEvents():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def clearScreen():
    # Use a color for now
    # TODO: Use a background image instead
    screen.fill("black")

#def updatePlayerPosition(dt):

# pygame setup
pygame.init()
screensize = (1280, 720)
screen = pygame.display.set_mode(screensize)

# Global variables
clock = pygame.time.Clock()
running = True
dt = 0
gravity = 0
objects = []

# player position in pixels
player = Player("Player 1", "red", pygame.Vector2(30,screensize[1]-25))


while running:
    checkEvents()
    # Update player from input and gravity
    # Update all other objects from gravity
    clearScreen()
    # Draw all objects

    # Add user input to player velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        #player.velocity.y -= 30
        player.thrust(30)
    #if keys[pygame.K_s]:
    #    player.velocity.y += 30
    if keys[pygame.K_a]:
        #player.velocity.x -= 30
        player.rotate(-5)
    if keys[pygame.K_d]:
        #player.velocity.x += 30
        player.rotate(5)

    # Add gravity
    player.velocity.y += gravity


    player.draw(screen, dt)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()