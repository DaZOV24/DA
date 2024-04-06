import pygame
from random import *
from pygame import *
pygame.init()



clock = time.Clock()
class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_w, player_h, player_x, player_y, player_speed):
         super().__init__()
         self.image = transform.scale(image.load(player_image), (player_w, player_h))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
     def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))





window = display.set_mode((640, 358))
display.set_caption('русская рулетка')
maf = transform.scale(image.load('maf.jpg'), (640, 358))    

# game = True
# while game:
#     background_image = pygame.image.load('maf.jpg').convert()
#     window.blit(background_image, (0, 0))
#     pygame.display.update()




# while True:
#     window.blit(background_image, (0, 0))
#     pygame.display.update()
#     clock.tick(60)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
























































display.update()
clock.tick(60)







