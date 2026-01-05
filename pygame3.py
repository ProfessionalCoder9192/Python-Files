from pygame import *
init()
screen = display.set_mode((400,300))
display.set_caption("Draw a rectangle.")
done = False
while not done:
    for e in event.get():
        if e.type == QUIT:
            done = True
    draw.rect(screen, (30, 18, 200), Rect(30, 30, 60, 60))
    display.flip()