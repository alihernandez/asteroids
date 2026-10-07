import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_TURN_SPEED
from player import Player
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver} \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(x, y)
   # print(screen.get_size())
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for draw in drawable:
            draw.draw(screen)
       # screen.fill("black")
       # player1.draw(screen) 
        pygame.display.flip()
       # player1.update(dt)
        dt = clock.tick(60) / 1000
        
        
    
if __name__ == "__main__":
    main()
