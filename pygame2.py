import pygame
pygame.init()
displaysurface = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Adding background image and image.")
backgroundimage = pygame.transform.scale(pygame.image.load("BackgroundImg.jpg").convert(),(500, 500))
marioimage = pygame.transform.scale(pygame.image.load("Mario.png").convert_alpha(),(200, 200))
mariorectangle = marioimage.get_rect(center = (250, 210))
text = pygame.font.Font(None, 36).render("Hello, Welcome to pygame.", True, pygame.Color("Red"))
textrectangle = text.get_rect(center = (250, 310))
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
    displaysurface.blit(backgroundimage,(0, 0))
    displaysurface.blit(marioimage, mariorectangle)
    displaysurface.blit(text, textrectangle)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()