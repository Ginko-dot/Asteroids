import pygame
from constants import *
from player import *

def main():
    pygame.init
    frame_limiter = pygame.time.Clock()
    dt= 0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        dt=frame_limiter.tick(60)/1000
        print (dt)

if __name__ == "__main__":
    main()
