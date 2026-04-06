import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("my first game screen")

background_color = (58, 58, 58)

image = pygame.Surface((300, 300))
image.fill((200, 0, 0)) 
image_rect = image.get_rect(center=(250, 250))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)
    
    screen.blit(image, image_rect)

    pygame.display.flip()

pygame.quit()

