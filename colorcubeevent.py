import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event Color Change")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self):
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)

sprite1 = SimpleSprite((255, 0, 0), 100, 100, 150, 150)
sprite2 = SimpleSprite((0, 0, 255), 100, 100, 350, 150)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()