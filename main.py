import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape



def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Asteroids")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0

    #fonts/text
    black = (0,0,0)
    white = (255,255,255)
    font = pygame.font.Font(None, 36)
    text= font.render("", True, white)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Shot.containers = (updatable, drawable, shots)

    Player.containers = (updatable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    lives = 3
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for entity in updatable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player) == False:
                lives -= 1
                player.kill()
                asteroid.kill()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                if lives < 0:
                    text = font.render("GAME OVER!", True, white)
                    lives = 0
                    player.kill()
                    asteroid.kill()
            
            
            for shot in shots:
                if shot.collision(asteroid) == False:
                    pygame.sprite.Sprite.kill(shot)
                    asteroid.split()
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        score += 100
                    if asteroid.radius > ASTEROID_MIN_RADIUS and asteroid.radius < ASTEROID_MAX_RADIUS:
                        score += 50
                    if asteroid.radius >= ASTEROID_MAX_RADIUS:
                        score += 25
            
        screen.fill("black")
        lives_text = font.render(f'Lives: {lives}', True, white)
        score_text = font.render(f'Score: {score}', True, white)
        screen.blit(lives_text, (1150, 10))
        screen.blit(score_text, (10, 10))
        screen.blit(text, text_rect)

        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()