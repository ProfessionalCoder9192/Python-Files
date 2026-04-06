import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Collision Score Game")

font = pygame.font.SysFont("Arial", 30)
score = 0

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

player = Sprite((0, 120, 255), 400, 300)
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

for i in range(7):
    enemy_x = random.randint(0, width - 40)
    enemy_y = random.randint(0, height - 40)
    enemy = Sprite((255, 50, 50), enemy_x, enemy_y)
    enemies.add(enemy)
    all_sprites.add(enemy)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.left > 0:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT] and player.rect.right < width:
        player.rect.x += 5
    if keys[pygame.K_UP] and player.rect.top > 0:
        player.rect.y -= 5
    if keys[pygame.K_DOWN] and player.rect.bottom < height:
        player.rect.y += 5

    hit_list = pygame.sprite.spritecollide(player, enemies, False)
    for hit in hit_list:
        score += 1
        hit.rect.x = random.randint(0, width - 40)
        hit.rect.y = random.randint(0, height - 40)

    screen.fill((20, 20, 20))
    all_sprites.draw(screen)
    
    score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
