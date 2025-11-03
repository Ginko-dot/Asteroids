import pygame
from constants import *

def main():
    pygame.init
    frame_limiter = pygame.time.Clock()
    dt= 0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip
        dt=frame_limiter.tick(60)/1000
        print (dt)

if __name__ == "__main__":
    main()
