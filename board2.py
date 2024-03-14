import pygame
import os
import random
pygame.init()

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

RUNNING = [pygame.image.load(os.path.join("assets", "DinoRun1.png")),
           pygame.image.load(os.path.join("assets", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("assets", "DinoJump.png"))
#DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
#           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("assets", "SmallCactus1.png")),
                pygame.image.load(os.path.join("assets", "SmallCactus2.png")),
                pygame.image.load(os.path.join("assets", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("assets", "LargeCactus1.png")),
                pygame.image.load(os.path.join("assets", "LargeCactus2.png")),
                pygame.image.load(os.path.join("assets", "LargeCactus3.png"))]

#BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        #pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

#CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("assets", "Track.png"))

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




#============================================================
pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('pygame window')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('assets/DinoRun1.png')



x =  80
y = 310


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.running_sprites = []
        self.ducking_sprites = []

        gameDisplay.blit(carImg, (x,y))

        def update(self, userInput):

            if userInput[pygame.K_UP]:
                x =  80
                y = 350
                
            elif userInput[pygame.K_DOWN]:
              
                x =  80
                y = 330

while not crashed:
    clock = pygame.time.Clock()
    points = 0
    game_speed = 20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        # this is the list with the keys being pressed
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            DinoImg = pygame.image.load('assets/DinoJump.png')
            y = 230
            DinoImg = pygame.image.load('assets/DinoRun1.png')
            #pygame.time.delay (2000)

        


            #y = 310
    
        if keys[pygame.K_DOWN]:
            DinoImg = pygame.image.load('assets/DinoJump.png')
            y = 270
            DinoImg = pygame.image.load('assets/DinoRun1.png')

        # we update the screen at every frame
        pygame.display.flip()
        # if we put the frame rate at 60 the sprite will move slower
        clock.tick(20)

        def score():
            global points, game_speed
            points += 1
            if points % 100 == 0:
                game_speed += 1

            #text = font.render("Points: " + str(points), True, (0, 0, 0))
            #textRect = text.get_rect()
            #textRect.center = (1000, 40)
            #SCREEN.blit(text, textRect)


   
    

    gameDisplay.fill(white)
    Car(x, y)

    pygame.display.update()
  

pygame.quit()
quit()