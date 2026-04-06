import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

font = pygame.font.SysFont("Arial", 36)
text_surface = font.render("Hello World", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(320, 150))

rect_color = (0, 150, 255)
rect_width, rect_height = 120, 80
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()