import pygame
from random import *
from pygame import *
pygame.init()



clock = time.Clock()












window = display.set_mode((1080, 720))
display.set_caption('русская рулетка')
maf = transform.scale(image.load('maf1.jpg'), (1080, 720))    
pistolet = transform.scale(image.load('gun1488.png'), (350, 350))  



game = True
while game:
    window.blit(maf, (0, 0))
    window.blit(pistolet, (360, 400))

    for e in event.get():
        if e.type == QUIT:
            game = False

    pygame.display.update()
    clock.tick(60)























































display.update()
clock.tick(60)







