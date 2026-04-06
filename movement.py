import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Movement Game")

class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

player = RectSprite((0, 255, 0), 50, 50, 100, 300)
static_box = RectSprite((255, 0, 0), 50, 50, 500, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(static_box)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-player.speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.speed, 0)
    if keys[pygame.K_UP]:
        player.move(0, -player.speed)
    if keys[pygame.K_DOWN]:
        player.move(0, player.speed)

    screen.fill((30, 30, 30))
    
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
