import pygame
import time
from pygame.constants import KEYUP
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    KEYUP,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Initialize pygame
pygame.init()

#adding cacti enemy to the game as a custom event in pygame
#add_cacti = pygame.USEREVENT + 1
#pygame.time.set_timer(add_cacti, 250)

# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Dino(pygame.sprite.Sprite):
    def __init__(self, dino_y_pos):
        super(Dino, self).__init__()
        self.y_pos = dino_y_pos
        self.surf = pygame.image.load("assets/DinoRun1.png")
        self.rect = self.surf.get_rect(center = (50, self.y_pos))

        self.track = pygame.image.load("assets/track.png")
        self.track_rect = self.track.get_rect(center=(0,300))
    def update_dino(self):
        #starttime = time.time()
        self.y_pos -= 100
        self.surf = pygame.image.load("assets/DinoRun1.png")
        self.rect = self.surf.get_rect(center=(50, self.y_pos))
        """
        while time.time() - starttime < 1:
            self.surf = pygame.image.load("assets/DinoRun1.png")
            self.rect = self.surf.get_rect(center=(50, self.y_pos))
            screen.blit(self.surf, self.rect)
            pygame.display.flip()
            
        self.y_pos += 100
        self.surf = pygame.image.load("assets/DinoRun1.png")
        self.rect = self.surf.get_rect(center=(50, self.y_pos))
        """
    def dino_down(self):
        self.y_pos += 100
        self.surf = pygame.image.load("assets/DinoRun1.png")
        self.rect = self.surf.get_rect(center=(50, self.y_pos))
    #use a timer for x seconds, another function that moves the height back to the original 
class Cacti(pygame.sprite.Sprite):
    list_of_cactus = []
    def __init__(self, x_pos):
        super(Cacti, self).__init__()
        self.x_pos = x_pos
        self.y_pos = 300
        self.surf = pygame.image.load("assets/LargeCactus1.png")
        self.rect = self.surf.get_rect(center=(self.x_pos, self.y_pos))
    def update(self):
        self.x_pos -= 2
        self.surf = pygame.image.load("assets/LargeCactus3.png")
        self.rect = self.surf.get_rect(center=(self.x_pos, self.y_pos))
    def remove(self):
        cacti_group.remove(cacti_group)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))


# Instantiate dinosaur
player = Dino(300)

#adding dino to the sprite group and making empty sprite groups
cacti_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group() 
dino_sprites = []
dino_sprites.append(player)
all_sprites.add(player) #only doing this here bc we don't need multple dinos 

# Variable to keep the main loop running
running = True
track_x_pos = 0
cacti_x_coord = SCREEN_WIDTH 

new_cacti = Cacti(cacti_x_coord)
Cacti.list_of_cactus.append(new_cacti)
all_sprites.add(new_cacti)


# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        #if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
        #    if event.key == K_ESCAPE:
        #        running = False
        # Check for QUIT event. If QUIT, then set running to false.
        if event.type == QUIT:
            running = False
        #keys = pygame.key.get_pressed()
        if event.type == KEYUP:
            starttime = time.time()
            player.update_dino()
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            # Update the display
            pygame.display.flip()
            while time.time() - starttime < 1:
                if Cacti.list_of_cactus[0].x_pos <= 0:
                    cacti_popped = Cacti.list_of_cactus[0]
                    Cacti.list_of_cactus.pop(0) #removing first cactus in list
                    #Change the new cactus index to be at the back of the list 
                    cacti_popped.x_pos = SCREEN_WIDTH
                    Cacti.list_of_cactus.append(cacti_popped)
                    #cacti_group.remove(cacti_group)
                elif new_cacti.x_pos == SCREEN_WIDTH/2:
                        cactus2 = Cacti(cacti_x_coord)
                        all_sprites.add(cactus2)
                        Cacti.list_of_cactus.append(cactus2)
                for i in Cacti.list_of_cactus:
                    i.update()
                for entity in all_sprites:
                    screen.blit(entity.surf, entity.rect)
            player.dino_down()
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            # Update the display
            pygame.display.flip()
        #elif event.type == KEYDOWN:
        #    player.dino_down()
            # update the interface
            #surf = pygame.image.load("assets/DinoRun1.png")
            #dino_updated = surf.get_rect(center = (50, Dino.dino_y_pos))
        """
        elif event.type == add_cacti:
            new_cacti = Cacti(cacti_x_coord)
            cacti_group.add(new_cacti)
            all_sprites.add(new_cacti)
            screen.fill((255, 255, 255))
            """
    #removing cacti if its beyond width 
    if Cacti.list_of_cactus[0].x_pos <= 0:
        cacti_popped = Cacti.list_of_cactus[0]
        Cacti.list_of_cactus.pop(0) #removing first cactus in list
        #Change the new cactus index to be at the back of the list 
        cacti_popped.x_pos = SCREEN_WIDTH
        Cacti.list_of_cactus.append(cacti_popped)
        #cacti_group.remove(cacti_group)
    elif new_cacti.x_pos == SCREEN_WIDTH/2:
            cactus2 = Cacti(cacti_x_coord)
            all_sprites.add(cactus2)
            Cacti.list_of_cactus.append(cactus2)
            #cactus2.update()
    #new_cacti.update()

    #if keys[pygame.K_UP]:
        #Dino.dino_y_pos += 100

    for i in Cacti.list_of_cactus:
        i.update()

    track_x_pos -= 2
    if track_x_pos <= -1200:
        track_x_pos = 0
        
    screen.fill((255, 255, 255))
    #Draw the player on the screen
    #screen.blit(player.surf, (20, 220))
    screen.blit(player.track, (track_x_pos, 300))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    # Update the display
    pygame.display.flip()