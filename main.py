import pygame,sys
from asteroidfield import *
from logger import log_state, log_event
from constants import *
from player import *
from asteroid import *
#from circleshape import *

def main():
    pygame.init()
    font = pygame.font.SysFont("Arial", 48)
    frame_limiter = pygame.time.Clock()
    dt= 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable)
    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
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
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print ("Game over!")
                text_surface = font.render("GAME OVER", True, (255, 0, 0))
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                screen.blit(text_surface, text_rect)
                pygame.display.flip()
    
                pygame.time.wait(5000) #wait 5 seconds to shutdown
                sys.exit()
                sys.exit()
        screen.fill((0,0,0))
        for entity in drawable:
            entity.draw(screen)
            #print("drawing:", entity)
        pygame.display.flip()
        dt=frame_limiter.tick(60)/1000
        #print (dt)

if __name__ == "__main__":
    main()
