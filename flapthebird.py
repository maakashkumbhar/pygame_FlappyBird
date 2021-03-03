import pygame
import random
import sys
from pygame.locals import *

### Global Variables ###
SCREEN_HEIGHT = 511
SCREEN_WIDTH = 289
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
FPS = 60
GROUNDY = SCREEN_HEIGHT*0.8
base_move = 0
list_of_pipes = []
GRAVITY = -2
player_newPos = 0 
##Pygame init##
pygame.init()
#######Resources##########
background_img = pygame.image.load('gallery/sprites/background.png').convert_alpha()
base_img = pygame.image.load('gallery/sprites/base.png').convert_alpha()
pipe_img = pygame.image.load('gallery/sprites/pipe.png').convert_alpha()
TIMER = pygame.USEREVENT
pygame.time.set_timer(TIMER,800)
player_img = pygame.image.load('gallery/sprites/bird.png').convert_alpha()
player_rect = player_img.get_rect(center=(90,SCREEN_WIDTH/2))
#############################

def base_movement(baseposX,baseposY):
    SCREEN.blit(base_img,(baseposX,baseposY))
    #SCREEN.blit(base_img,(baseposX+150,baseposY))

def pipes_movement(list_of_pipes,pipe_img):
    for pipe in list_of_pipes:
        pipe.centerx -= 1

    for pipe in list_of_pipes:
        SCREEN.blit(pipe_img,pipe)
def player_movement(player_img,player_rect):
    SCREEN.blit(player_img,player_rect)


if __name__ == "__main__":

    clock = pygame.time.Clock()
    running = True
    while running:
        print(list_of_pipes)
        SCREEN.blit(background_img,(0,0))
        pipes_movement(list_of_pipes,pipe_img)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
                sys.exit()
            if event.type == TIMER:
                height_of_pipes = [300,350,390,480,500,400,450]
                pipe_rect = pipe_img.get_rect(midtop = (290,random.choice(height_of_pipes)))
                list_of_pipes.append(pipe_rect)
            
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player_newPos = player_newPos/3 +20
                    player_newPos += 10
            if event.type == KEYUP:
                if event.key == K_SPACE:
                    player_newPos -= 10

        base_move += -1
        base_movement(base_move,GROUNDY)
        ###
        if base_move <= -50:
            base_move = 0
        ###
        #####Player movement######
        player_newPos -= GRAVITY
        player_rect.centery = player_newPos
        player_movement(player_img,player_rect)

        ###############################
        clock.tick(FPS)
        pygame.display.update()


