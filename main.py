from pygame import * 
from random import *



clock = time.Clock()
window = display.set_mode((1080, 720))
display.set_caption('русская рулетка')


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
























































display.update()
clock.tick(60)

