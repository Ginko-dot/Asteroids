import pygame
from logger import log_state
from constants import *
from player import *

def main():
    pygame.init()
    frame_limiter = pygame.time.Clock()
    dt= 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #print("updatable size:", len(updateable))
    #print("drawable size:", len(drawable))


    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill((0,0,0))
        for entity in drawable:
            entity.draw(screen)
            #print("drawing:", entity)
        pygame.display.flip()
        dt=frame_limiter.tick(60)/1000
        #print (dt)

if __name__ == "__main__":
    main()
