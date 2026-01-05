from pygame import *
init()
screen = display.set_mode((400, 400))
screen.fill((255, 255, 255))
display.set_caption("Draw a rectangle.")
draw.circle(screen, (0, 255, 0), (300, 300), (50))
draw.circle(screen, (0, 255, 0), (100, 100), (50), 3)
running = False
while not running:
    for e in event.get():
        if e.type == QUIT:
            running = True
    display.flip()
quit()