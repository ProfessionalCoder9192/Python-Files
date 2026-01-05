from pygame import *
init()
screen = display.set_mode((500, 500))
display.set_caption("color changing sprite")
colors = {
    "red":Color("red"),
    "green":Color("green"),
    "orange":Color("orange"),
    "blue":Color("blue"),
    "purple":Color("purple")
}
currentColor = colors["purple"]
x,y = 30,30
spritewidth, spriteheight = 60, 60
clock = time.Clock()
running = False
while not running:
    for e in event.get():
        if e.type == QUIT:
            running = True
    pressed = key.get_pressed()
    if pressed[K_LEFT]:x=x-3
    if pressed[K_RIGHT]:x=x+3
    if pressed[K_UP]:y=y-3
    if pressed[K_DOWN]: y=y+3
    x=min(max(0,x), 500-spritewidth)
    y=min(max(0,y), 500-spriteheight)
    if x == 0:
        currentColor = colors["red"]
    elif x == 500-spritewidth:
        currentColor = colors["orange"]
    elif y == 0:
        currentColor = colors["green"]
    elif y == 500-spriteheight:
        currentColor = colors["blue"]
    else:
        currentColor = colors["purple"]
    screen.fill((Color("white")))
    draw.rect(screen, currentColor, (x,y,spritewidth,spriteheight))
    display.flip()
    clock.tick(90)
quit()