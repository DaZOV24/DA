import pygame
from random import *
from pygame import *
pygame.init()

score = 0 

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



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()


font.init()
font2 = font.Font(None, 36)





window = display.set_mode((1080, 720))
display.set_caption('русская рулетка')
maf = transform.scale(image.load('fon.jpg'), (1080, 720))    
pistolet = transform.scale(image.load('gun1488.png'), (350, 350))  

mixer.init()
mixer.music.load('enit.mp3')
skrimep = mixer.Sound('skrimep2.mp3')
mixer.music.play()
pistoletda = mixer.Sound('pistoletda2remix2.mp3')
finish = False
player = 1
game = True
while game:
    if finish != True:
        window.blit(maf, (0, 0))
        window.blit(pistolet, (360, 400))
        tex1 = font2.render('Сейчас ходит игрок '+str(player)+':', 1, (128, 128, 128))
        window.blit(tex1, (30, 60))
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if player == 1:
                        score += 1
                        x = randint(1, 8)
                        player = 2
                        if x == 1:
                            pistoletda.play()
                            finish = True

            if e.type == MOUSEBUTTONUP:
                if e.button == 3:
                    if player == 2:
                        score += 1
                        x = randint(1, 8)
                        player = 1
                        if x == 1:
                            pistoletda.play()
                            finish = True    
        tex1 = font2.render('Кол-во выстрелов: ' + str(score), 1, (255, 255, 255))
        window.blit(tex1, (10, 20))
    else:
        skrimep.play()
        font3 = font.Font(None, 240)
        lose = font3.render('СМЕРТЬ', True, (255, 0, 0))
        window.blit(lose, (250, 300))


    for e in event.get():
        if e.type == QUIT:
            game = False
                   
    
    pygame.display.update()
    clock.tick(60)
























display.update()
clock.tick(60)







