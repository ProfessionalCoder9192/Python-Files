import pygame
import random
import math

pygame.init()
pygame.mixer.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

""" 
To use your own files, place them in the same folder and 
replace the names below (e.g., 'background.png', 'laser.wav')
"""

try:
    background = pygame.image.load('background.png')
except:
    background = pygame.Surface((screen_width, screen_height))
    background.fill((10, 10, 25))

try:
    shoot_sound = pygame.mixer.Sound('laser.wav')
    explosion_sound = pygame.mixer.Sound('explosion.wav')
except:
    shoot_sound = None
    explosion_sound = None

score_val = 0
font = pygame.font.SysFont("Arial", 32)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(midbottom=(400, 580))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1

    def update(self):
        self.rect.x += 2 * self.direction
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

player = Player()
all_sprites = pygame.sprite.Group(player)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for row in range(4):
    for col in range(10):
        enemy = Enemy(80 + col * 60, 50 + row * 50)
        enemies.add(enemy)
        all_sprites.add(enemy)

clock = pygame.time.Clock()
running = True

while running:
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullets.add(bullet)
                all_sprites.add(bullet)
                if shoot_sound: shoot_sound.play()

    all_sprites.update()

    enemy_hit_edge = False
    for enemy in enemies:
        if enemy.rect.right >= screen_width or enemy.rect.left <= 0:
            enemy_hit_edge = True
            break
    
    if enemy_hit_edge:
        for enemy in enemies:
            enemy.direction *= -1
            enemy.rect.y += 10

    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score_val += 10
        if explosion_sound: explosion_sound.play()

    if pygame.sprite.spritecollideany(player, enemies) or not enemies:
        running = False

    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score_val}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
