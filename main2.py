font.init()
font2 = font.Font(None, 36)





window = display.set_mode((1080, 720))
display.set_caption('русская рулетка')
maf = transform.scale(image.load('fon.jpg'), (1080, 720))    
pistolet = transform.scale(image.load('gun1488.png'), (350, 350))  

mixer.init()
# mixer.music.load('enit.mp3')
# skrimep = mixer.Sound('skrimep2.mp3')
baranan = mixer.Sound('baranan.mp3')
# mixer.music.play()
pistoletda = mixer.Sound('pistoletda2remix2.mp3')
finish = False
player = 1
game = True

gamestart = False
mode = 0
    
while game:
    if gamestart == False:
        # Меню
        tex11 = font2.render('Добро пожаловать в игру ''Русскую рулетку''', 1, (128, 128, 128))
        window.blit(tex11, (250, 100))
        tex11 = font2.render('Если хотите играть с ботом, нажмите ''Q''', 1, (128, 128, 128))
        window.blit(tex11, (250, 250))
        tex11 = font2.render('Если хотите онлайн, нажмите ''E''', 1, (128, 128, 128))          
        window.blit(tex11, (250, 220))



    else:
        if finish != True:
            if mode == 1:
                # Игра с человеком

                window.blit(maf, (0, 0))
                window.blit(pistolet, (360, 400))
                tex11 = font2.render('Сейчас ходит игрок '+str(player)+':', 1, (128, 128, 128))
                window.blit(tex11, (30, 60))
                
                        
                tex1 = font2.render('Кол-во выстрелов: ' + str(score), 1, (255, 255, 255))
                window.blit(tex1, (10, 20))
            if mode == 2:
                # Bot
                window.blit(maf, (0, 0))
                window.blit(pistolet, (360, 400))
                tex11 = font2.render('Сейчас ходит игрок '+str(player)+':', 1, (128, 128, 128))
                window.blit(tex11, (30, 60))
                
                        
                tex1 = font2.render('Кол-во выстрелов: ' + str(score), 1, (255, 255, 255))
                window.blit(tex1, (10, 20))
                if player == 2:
                    x = randint(1, 8)
                    player = 1
                    if x == 1:
                        pistoletda.play()
                        finish = True

                        

        else:
            # Проигрыш

            # skrimep.play()
            font3 = font.Font(None, 240)
            lose = font3.render('СМЕРТЬ', True, (255, 0, 0))
            window.blit(lose, (250, 300))
            tex1 = font2.render('Если хотите переиграть раунд, нажмите пробел', 1, (235, 235, 235))
            window.blit(tex1, (300, 250))
            tex1 = font2.render('Если хотите выйти в меню, нажмите H', 1, (235, 235, 235))
            window.blit(tex1, (350, 470))
            score = 0
            player = 1
            





    for e in event.get():
        if gamestart == True:
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if finish == True:
                        finish = False
            if e.type == KEYDOWN:
                if e.key == K_h:
                    gamestart = False
                    window.fill((0,0,0))
                    finish = False
                    
            
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    if player == 1:
                        
                        score += 1
                        x = randint(1, 8)
                        player = 2
                        if x == 1:
                            pistoletda.play()
                            finish = True
                        else:
                            baranan.play()


            if e.type == MOUSEBUTTONUP:
                if e.button == 3:
                    if mode == 1:
                        if player == 2:
                            score += 1
                            x = randint(1, 8)
                            player = 1
                            if x == 1:
                                pistoletda.play()
                                finish = True
                            else:
                                baranan.play()

        
        if e.type == KEYDOWN:
            if e.key == K_e:
                mode = 1
                gamestart = True
                baranan.play()
            if e.type == KEYDOWN:
                if e.key == K_q:
                    mode = 2
                    gamestart = True           
                    baranan.play()
        if e.type == QUIT:
            game = False
            # if score == 9:
            #     font3 = font.Font(None, 200) 
            #     lose = font3.render('Патроны кончились!', True, (0, 55, 55))
            #     window.blit(lose, (200, 300))
            #     game = False



    pygame.display.update()
    clock.tick(60)






























