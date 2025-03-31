# Pygame game template

import pygame
import sys
import config  
import random
import shapes

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock() 
    
    background_image = pygame.image.load('saturn_family1.jpg').convert()
    player_image = pygame.image.load('player.png').convert()
    player_image.set_colorkey(config.BLACK)


    running = True
    while running:
        running = handle_events()
        screen.blit(background_image,[0,0])
        player_position = pygame.mouse.get_pos()
        x = player_position[0]-40
        y = player_position[1]-30
        screen.blit(player_image,[x,y])
        pygame.display.flip()

        
        clock.tick(config.FPS)
    



    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
