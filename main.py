import pygame
import random
from pygame.constants import K_ESCAPE, KEYDOWN

#initializing a board with width and height defined 
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((255, 255, 255))
pygame.quit()
#import images

surf = pygame.Surface((50,50))
surf.fill((0,0,0))
rect = surf.get_rect()

class Dinosaur:

    #initialize the booleans for duck run and jump
    def __init__(self):
        #initialize duck_img , run_img, and jump_img to the images 
        self.duck = False
        self.run = True
        self.jump = False

    def run():
        ...
    def jump():
        ...
    def duck():
        ...
    #define coordinates of dinosaur 
    x_coord = 90
    y_coord = 300
    y_coord_duck = 270
   
class Obstacle:
    def __init__(self):
        ...


def main():
    #a while loop that updates the condition for running (as in the gam running)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False
    # we will need a way to update the bird